import perfcat  # noqa
import secrets
from nicegui import ui, app

app.native.window_args["resizable"] = True
app.native.window_args["text_select"] = True
app.native.start_args["debug"] = False

ui.run(
    native=True,
    reload=False,
    window_size=(1280, 768),
    title="Performance Catcher 2",
    storage_secret=secrets.token_hex(16),
)
