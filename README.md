# Genesal Jr. — repo base

Tu punto de partida para el reto de la semana. Lee `02_ENUNCIADO_SANDBOX.md`
(te lo pasa tu mentor) para saber **qué** construir. Esto explica **cómo arrancar**.

## 1. Entorno (día 1)

```bash
# 1. Crea y activa el entorno virtual
python -m venv venv
source venv/bin/activate        # macOS/Linux
# .\venv\Scripts\activate       # Windows

# 2. Instala dependencias
pip install -r requirements.txt

# 3. Copia el archivo de entorno (el .env real NUNCA se commitea)
cp .env.example .env

# 4. Crea el proyecto Django (si aún no existe)
django-admin startproject config .

# 5. Primeras migraciones + superusuario (para el admin)
python manage.py migrate
python manage.py createsuperuser

# 6. Arranca
python manage.py runserver
```

Abre http://127.0.0.1:8000/ y http://127.0.0.1:8000/admin/ — si ves ambas, +10 pts 🎉

## 2. Checklist antes de tu primer commit

- [ ] `git status` NO muestra `.env` ni `venv/` (el `.gitignore` ya los protege).
- [ ] Trabajas en una **rama**, no en `main` (créala desde GitLab, no desde PyCharm).
- [ ] El código está en **inglés**.

## 3. Correr los tests

```bash
pytest
```

## 4. Desplegar en Vercel

Vercel detecta Django por `manage.py` y usa `config/asgi.py` como entrypoint
(configurado en `pyproject.toml`). El build ejecuta las migraciones
automáticamente y Vercel sirve los estáticos tras `collectstatic`.

1. Crea una base de datos PostgreSQL (por ejemplo [Neon](https://neon.tech)) y
   copia su connection string.
2. Importa el repo en Vercel y define estas variables de entorno (Project
   Settings → Environment Variables):

   ```
   SECRET_KEY=<clave-larga-y-secreta>
   DATABASE_URL=postgresql://user:password@host/db?sslmode=require
   DEBUG=False
   ALLOWED_HOSTS=localhost,127.0.0.1,.vercel.app
   CORS_ALLOWED_ORIGINS=https://tu-frontend.vercel.app
   CSRF_TRUSTED_ORIGINS=https://*.vercel.app
   ```

3. Despliega con Git o con la CLI:

   ```bash
   vercel --prod
   ```

> `DATABASE_URL` es obligatoria en Vercel: el filesystem serverless es de solo
> lectura y SQLite no persiste datos. En local, si no la defines, se usa SQLite.

## 5. Convención de ramas

```
feature/<numero-issue>-descripcion-corta
# ej: feature/3-project-serializer-validation
```

## 6. Estructura que acabarás teniendo (orientativa)

```
config/              # settings, urls raíz
catalogue/           # tu app principal
├── models.py        # Project, Asset
├── serializers.py   # validación de negocio (Regla 1)
├── permissions.py   # scoping + anti-trampa (Reglas 2 y 3)
├── views.py         # ViewSets DELGADOS
├── urls.py          # router
└── tests/           # pytest
```

> Fíjate: `permissions.py` y `serializers.py` son archivos **separados**. Así está
> montado el Aurora real. Mantén cada cosa en su sitio.
