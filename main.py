import perfcat
import secrets
from nicegui import ui,app
from perfcat import config

app.native.window_args['resizable'] = True
app.native.window_args['url'] = config.url
app.native.start_args['debug'] = True

ui.run(native=True,window_size=(1280,768),title="PerformanceCatcher",storage_secret=secrets.token_hex(16))