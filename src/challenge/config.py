from decouple import config

DB_POSTGRESQL_HOST = config("DB_POSTGRESQL_HOST", default="localhost")
DB_POSTGRESQL_USER = config("DB_POSTGRESQL_USER", default="postgres")
DB_POSTGRESQL_PASSWORD = config("DB_POSTGRESQL_PASSWORD", default="postgres")
DB_POSTGRESQL_DB = config("DB_POSTGRESQL_DB", default="app_db")
DB_POSTGRESQL_URI = f"postgresql://{DB_POSTGRESQL_USER}:{DB_POSTGRESQL_PASSWORD}@{DB_POSTGRESQL_HOST}:5432/{DB_POSTGRESQL_DB}"

DB_SQLITE_PATH = config("DB_SQLITE_PATH", default="sqlite:///database.db")
