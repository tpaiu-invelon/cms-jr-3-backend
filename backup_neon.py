import sqlite3
from datetime import datetime
from pathlib import Path


# Directorio del proyecto
BASE_DIR = Path(__file__).resolve().parent

# Base de datos SQLite
DATABASE = BASE_DIR / "db.sqlite3"

# Carpeta de backups
BACKUP_DIR = BASE_DIR / "backups"


def create_backup():

    if not DATABASE.exists():
        print("ERROR: No se encuentra db.sqlite3")
        return

    BACKUP_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    backup_file = BACKUP_DIR / f"backup_{timestamp}.sql"

    try:
        with sqlite3.connect(DATABASE) as connection:

            with open(backup_file, "w", encoding="utf-8") as file:

                for line in connection.iterdump():
                    file.write(line + "\n")

        print("Backup realizado correctamente.")
        print(f"Archivo: {backup_file}")
        print(f"Tamaño: {backup_file.stat().st_size / 1024:.2f} KB")

    except sqlite3.Error as error:
        print(f"Error SQLite: {error}")

    except OSError as error:
        print(f"Error de archivo: {error}")


if __name__ == "__main__":
    create_backup()