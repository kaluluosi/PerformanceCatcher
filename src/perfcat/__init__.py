import perfcat
from perfcat import pages,logger # type: ignore  # noqa: F401
from nicegui import app
from importlib import resources

with resources.path(perfcat,"static") as path:
    app.add_static_files("/static",path.as_posix())

with resources.path(perfcat,"media") as path:
    app.add_static_files("/media",path.as_posix(),)

