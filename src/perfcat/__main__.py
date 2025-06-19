from nicegui import ui,app
app.native.window_args['resizable'] = True
app.native.start_args['debug'] = True

ui.run(native=True,reload=False,window_size=(1024,768),title="PerformanceCatcher",frameless=False)