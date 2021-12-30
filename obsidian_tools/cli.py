import typer
import logging
import asyncio

from pathlib import Path

from obsidian_tools.watch import main

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")

ch = logging.StreamHandler()

ch.setFormatter(formatter)

logging.getLogger("").setLevel(logging.WARNING)
logging.getLogger("").addHandler(ch)

log = logging.getLogger(__name__)


app = typer.Typer()


@app.command()
def watch(
    target: Path = typer.Argument(
        ...,
        exists=True,
        file_okay=True,
        dir_okay=False,
        writable=True,
        readable=True,
        resolve_path=True,
    )
):
    asyncio.run(main(target))


@app.callback(invoke_without_command=True)
def main_cli(ctx: typer.Context, debug: bool = typer.Option(False)):
    if debug:
        logging.getLogger("").setLevel(logging.DEBUG)

    if ctx.invoked_subcommand is not None:
        return

    print("Welcome to obsidian-tools")


app()
