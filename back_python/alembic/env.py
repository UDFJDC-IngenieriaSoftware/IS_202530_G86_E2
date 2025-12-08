from alembic import context
# Importar los modelos para que Alembic los conozca
from model import Carer, Patient, Carer_Patient, Treatment, Medicine, Reminder
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

config = context.config

fileConfig(config.config_file_name)

from db.database import Base

# Fuerza registro de los modelos
import model

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Ejecuta migrations en modo offline."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Ejecuta migrations en modo online."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
