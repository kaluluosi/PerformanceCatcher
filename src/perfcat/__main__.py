from nicegui import ui, app

if __name__ == "__main__":
    app.native.window_args["resizable"] = True
    app.native.start_args["debug"] = True
    app.native.window_args["text_select"] = True

    ui.run(
        native=True,
        reload=False,
        window_size=(1024, 768),
        title="Performance Catcher",
        frameless=False,
    )
