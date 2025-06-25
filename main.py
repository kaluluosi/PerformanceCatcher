import perfcat
import secrets
from nicegui import ui, app
from perfcat import config
from importlib import resources

app.native.window_args["resizable"] = True
app.native.start_args["debug"] = True

ui.run(
    native=True,
    window_size=(1280, 768),
    title="PerformanceCatcher",
    storage_secret=secrets.token_hex(16),
)
