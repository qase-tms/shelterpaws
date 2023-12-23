from pathlib import Path

import typer

from alembic.config import Config
from alembic import command

from backend.settings import Settings

cli = typer.Typer()
alembic_cli = typer.Typer()
cli.add_typer(alembic_cli, name="alembic")

settings = Settings()
PROJECT_PATH = Path(__file__).parent.resolve()
ALEMBIC_CONFIG = PROJECT_PATH / "alembic.ini"
ALEMBIC_SCRIPT = PROJECT_PATH

config = Config(ALEMBIC_CONFIG)
config.set_main_option("sqlalchemy.url", settings.database_url)
config.set_main_option("script_location", str(ALEMBIC_SCRIPT))


@alembic_cli.command(
    "makemigrations",
    help="Generate new migration",
)
def generate_revision(message: str = typer.Argument(
    None,
    help="An optional field is used to specify the comment of the revision."
)):
    command.revision(config, message, autogenerate=True)


@alembic_cli.command(
    "upgrade",
    help="Upgrade revision."
)
def upgrade_revision(name_revision: str = typer.Argument(
    "head",
    help="An optional field is used to specify the name of the revision.",
    metavar="revision",
)):
    command.upgrade(config, name_revision)


@alembic_cli.command(
    "stamp",
    help="Stamp revision."
)
def stamp_revision(name_revision: str = typer.Argument(
    "head",
    help="An optional field is used to specify the name of the revision.",
    metavar="revision",
)):
    command.stamp(config, name_revision)


@alembic_cli.command(
    "downgrade",
    help="Downgrade revision.",
)
def downgrade_revision(name_revision: str = typer.Argument(
    '-1',
    help="An optional field is used to specify the name of the revision.",
    metavar="revision",
)):
    command.downgrade(config, name_revision)


@alembic_cli.command(
    "merge",
    help="Merge revisions."
)
def merge_revisions(name: str = typer.Argument(
    "heads",
    help="An optional field is used to specify the name of the revision.",
    metavar="revision",
)):
    command.merge(config, name)


@alembic_cli.command(
    "history",
    help="History of revisions."
)
def history():
    command.history(config, indicate_current=True)


@alembic_cli.command(
    "url",
    help="Database url."
)
def url():
    print(config.get_main_option("sqlalchemy.url"))


if __name__ == "__main__":
    cli()
