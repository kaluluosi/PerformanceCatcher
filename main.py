import perfcat  # noqa
import secrets
from nicegui import ui, app

app.native.window_args["resizable"] = True
app.native.window_args["text_select"] = True
app.native.start_args["debug"] = True

ui.run(
    native=True,
    window_size=(1280, 768),
    title="Performance Catcher",
    storage_secret=secrets.token_hex(16),
)
