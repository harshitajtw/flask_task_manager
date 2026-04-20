import os
import logging
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.models import db
config = context.config
fileConfig(config.config_file_name)
logger = logging.getLogger("alembic.env")

# ---------------------------
# 1. ENV DB SELECTION
# ---------------------------
env = os.getenv("APP_ENV", "develop")

if env == "master":
    db_uri = "sqlite:///test_master.db"
else:
    db_uri = "sqlite:///test_develop.db"

config.set_main_option("sqlalchemy.url", db_uri)

# ---------------------------
# 2. METADATA
# ---------------------------
target_metadata = db.metadata


# ---------------------------
# OFFLINE MODE
# ---------------------------
def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


# ---------------------------
# ONLINE MODE
# ---------------------------
def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()