from nicegui import ui
from fastapi import Request
from perfcat.components.layout import frame

columns = [
    {'name': 'name', 'label': '属性', 'field': 'name', 'required': True, 'align': 'left'},
    {'name': 'value', 'label': '值', 'field': 'value', 'sortable': False},
]
rows = [
    {'name': 'Alice', 'age': 18},
    {'name': 'Bob', 'age': 21},
    {'name': 'Carol', 'age': None},  # 假设 Carol 的年龄未知，可以设置为 None
]

@ui.page('/android_profiler',title='Android Profier')
async def android_profier(request: Request):
    
    with frame():

        drawer = ui.drawer(side='right', value=True,elevated=True)

        with ui.page_sticky(position='top-right',y_offset=100).style("z-index:2000"):
            ui.button(icon="arrow_left",on_click=drawer.toggle).style("padding:10px 0px;border-radius:3px 0px 0px 3px;")

        with drawer.classes("p-0").props("width=400"):

            with ui.tabs() as tabs:
                device_panel = ui.tab("连接设备")
                monitor_panel = ui.tab("性能监视器")

            with ui.tab_panels(tabs,value=device_panel):
                with ui.tab_panel(device_panel).classes('p-0'):
                    # 设备连接面板
                    with ui.column().classes("p-4"):
                        with ui.card().tight().style("width:100%"):
                            with ui.card_section().style("width:100%").classes("flex gap-4"):
                                
                                with ui.row().classes('items-center w-full'):
                                    with ui.input("远程连接",placeholder="e.g 192.168.1.100:5555").classes("flex-1").props("dense").add_slot('prepend'):
                                        ui.icon("wifi")
                                    
                                    ui.button(icon="add").props("dense")

                                with ui.row().classes('items-center w-full'):
                                    with ui.select([1,2,3],label="选择设备").props("dense").classes("w-full flex-1").add_slot("prepend"):
                                        ui.icon("adb")
                                    
                                    with ui.button(icon="wifi").props("dense"):
                                        ui.tooltip("开启无线连接\n(adb tcpip:5555)")

                                with ui.select([1,2,3],label="选择APP").classes("w-full").props("dense").add_slot("prepend"):
                                    ui.icon("apps")
                                
                                with ui.select([1,2,3],label="选择进程").classes("w-full").props("dense").add_slot("prepend"):
                                    ui.icon("wysiwyg")

                                with ui.row().classes("items-center w-full justify-end"):
                                    ui.button(icon="link")
                                    ui.button(icon="lens").props("bg-color='primary' color=red")

                        with ui.card().tight().style("width:100%"):
                            ui.table(columns=columns,rows=rows).props("dense separator=cell bordered").classes("w-full")
                            with ui.card_section().style("width:100%").style("text-align:right"):
                                ui.button(icon="copy_all",on_click=lambda:ui.notification("已复制到剪贴板",position='top'))


        with ui.row().classes("size-full"):
            with ui.scroll_area().classes("flex-1 size-full p-0 min-w-96"):
                with ui.card().tight().style("width:100%"):
                    with ui.card_section():
                        ui.label('Lorem ipsum dolor sit amet, consectetur adipiscing elit, ...')