import contextlib
from nicegui import ui
from perfcat import config
from perfcat.utils import is_active_page


class Frame:
    navigationbar_expand = False

    def __init__(self) -> None:
        ui.query("main").style("height:92vh")
        ui.query("main .nicegui-content").style("height:100%")

        # 头
        with ui.header(elevated=True).classes('items-center').style("padding:0.3rem"):
            with ui.row().style("gap:0px;"):
                ui.button(icon="arrow_back",on_click=ui.navigate.back).props('flat color=white')
                ui.button(icon="menu",on_click=lambda: left_drawer.toggle()).props('flat color=white')
            ui.icon("insights")
            ui.label("Performance Catcher").classes("mr-auto")

            with ui.row().classes("gap-0"):
                ui.button(icon="minimize").props('flat color=white')
                ui.button(icon="fullscreen").props('flat color=white')
                ui.button(icon="close").classes("hover:bg-red-400").props('flat color=white')

        # 导航菜单
        with ui.left_drawer(fixed=False,elevated=True).style("padding:0px;").props("width=225") as left_drawer:
            left_drawer.bind_value(Frame,'navigationbar_expand')

            with ui.scroll_area().classes('mb-auto h-full') as scroll_area:

                content = ui.query(f"#{scroll_area.html_id} .q-scrollarea__content")
                content.classes("!p-0")

                # 路由菜单
                with ui.list().props('padding').classes("full-width"): 
                    for _, value in config.navigations.items():
                        with ui.item(on_click=lambda path=value['path']: ui.navigate.to(path)) as item: # type: ignore
                            item.props['active'] = is_active_page(value['path'])
                            with ui.item_section().props('avatar'):
                                ui.icon(value['icon'])
                            with ui.item_section():
                                ui.item_label(value['title'])

            # 固定设定栏
            with ui.list().props('padding bordered').classes("full-width"): 
                    with ui.item(on_click=lambda: ui.notification("Coming soon!")) as item: # type: ignore
                        with ui.item_section().props('avatar'):
                            ui.icon("settings")
                        with ui.item_section():
                            ui.item_label("Settings")

