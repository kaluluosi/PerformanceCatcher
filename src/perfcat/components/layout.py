from nicegui import ui
from contextlib import contextmanager
from perfcat import config


@contextmanager
def frame():

    # 内容区域
    with ui.column():
        yield
    
    with ui.header(elevated=True).classes('items-center'):
        with ui.row().style("gap:0px;"):
            ui.button(icon="arrow_back").props('flat color=white')
            ui.button(icon="menu",on_click=lambda: left_drawer.toggle()).props('flat color=white')
        ui.icon("insights")
        ui.label("Performance Catcher")


    with ui.left_drawer(fixed=False,elevated=True).style("padding:0px;") as left_drawer:
        left_drawer.bind_value(config,'navigationbar_toggle')

        with ui.list().props('padding').classes("full-width"): 
            for _, value in config.navigations.items():
                with ui.item(on_click=lambda path=value['path']: ui.navigate.to(path)) as item:
                    item.props['active'] = ui.context.client.page.path == value['path']
                    with ui.item_section().props('avatar'):
                        ui.icon(value['icon'])
                    with ui.item_section():
                        ui.item_label(value['title'])
    