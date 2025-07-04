from . import pages, logger  # noqa
from nicegui import app
from importlib import resources
from perfcat.services import AndroidProfielerService

with resources.path("perfcat", "static") as path:
    app.add_static_files("/static", path.as_posix())

with resources.path("perfcat", "media") as path:
    app.add_static_files(
        "/media",
        path.as_posix(),
    )

@app.on_shutdown
async def teardown(app):
    await AndroidProfielerService.stop_adb_server()