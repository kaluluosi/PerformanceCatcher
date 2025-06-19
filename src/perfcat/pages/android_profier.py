import re
from typing import cast
from nicegui import app, ui,events
from perfcat.components.layout import Frame
from perfcat.services.android_profiler_service import AndroidProfielerService
from perfcat.utils import notify

columns = [
    {'name': 'name', 'label': '属性', 'field': 'name', 'required': True, 'align': 'left'},
    {'name': 'value', 'label': '值', 'field': 'value', 'sortable': False},
]
rows = [
    {'name': 'Alice', 'age': 18},
    {'name': 'Bob', 'age': 21},
    {'name': 'Carol', 'age': None},  # 假设 Carol 的年龄未知，可以设置为 None
]


async def _create_drawer():
        drawer = ui.drawer(side='right', value=True,elevated=True)
        drawer.bind_value(app.storage.general,'drawer_expand')

        with ui.page_sticky(position='top-right',y_offset=100).style("z-index:2000"):
            ui.button(icon="arrow_left",on_click=lambda: drawer.toggle()).style("padding:10px 0px;border-radius:3px 0px 0px 3px;")

        with drawer.classes("p-0").props("width=400"):
            with ui.tabs() as tabs:
                device_panel = ui.tab("设备面板")
                

            with ui.tab_panels(tabs,value=device_panel):
                with ui.tab_panel(device_panel).classes('p-0'):
                        # 设备连接面板
                        await _create_device_control_panel()

async def _create_device_control_panel():
        with ui.column().classes("p-4"):
            await _create_remote_connect_card()
            await _create_device_card()
            await _create_deviceinfo_card()

async def _create_remote_connect_card():
        async def _remote_connect():
            text = cast(str,ip_input.value)
            if text:
                print("connect to",text)
                ip,port = text.split(":")
                res = await AndroidProfielerService.remote_connect(ip,int(port))
                if res:
                    notify(f"远程连接成功：{text}",position='bottom-right',type='positive',color='green')
                else:
                    notify(f"远程连接失败：{text}",position='bottom-right',type='negative',color='red')

        with ui.card().tight().style("width:100%"):
            with ui.card_section().style("width:100%").classes("flex gap-4"):
                with ui.row().classes('items-center w-full'):
                    def _ip_port_validation(v:str):
                        # 正则表达式来识别 ip:port 格式，要兼容localhost:port
                        pattern = re.compile(r'^((\d{1,3}\.){3}\d{1,3}|\blocalhost\b):(\d{1,5})$')
                        if pattern.match(v):
                            return None
                        else:
                            return "请输入正确的IP端口格式"

                    ip_input = ui.input("远程连接",placeholder="e.g 192.168.1.100:5555",validation=_ip_port_validation).classes("flex-1").props("dense")
                    with ip_input.add_slot('prepend'):
                        ui.icon("wifi")
                    
                    ui.button(icon="add",on_click=_remote_connect).props("dense")

async def _create_device_card():
        AndroidProfielerService.on_devices_changed.subscribe(
            lambda devices: device_select.set_options(devices)
            )
        
        AndroidProfielerService.on_device_connected.subscribe(
            lambda device: notify(f"设备连接：{device}",position='bottom-right',type='positive',color='green')
            )
        AndroidProfielerService.on_device_disconnected.subscribe(
            lambda device: notify(f"设备断开：{device}",position='bottom-right',type='negative',color='red')
        )


        with ui.card().tight().style("width:100%"):
            with ui.card_section().style("width:100%").classes("flex gap-4"):

                with ui.row().classes('items-center w-full'):
                    
                    async def _on_device_changed(v:events.ValueChangeEventArguments):
                        if v.value is None:
                            app_select.clear()
                            process_select.clear()
                            return
                        device = await AndroidProfielerService.get_device(v.value)
                        applist = await device.pm.list_packages()
                        app_select.set_options(applist)

                    device_select = ui.select([],label="选择设备",on_change=_on_device_changed).props("dense").classes("w-full flex-1")

                    with device_select.add_slot("prepend"):
                        ui.icon("adb")
                    
                    with ui.button(icon="wifi").props("dense"):
                        ui.tooltip("开启无线连接\n(adb tcpip:5555)")

                
                async def _on_app_changed(v:events.ValueChangeEventArguments):
                    device_sno = cast(str,device_select.value)
                    app_name = v.value
                    processes = await AndroidProfielerService.get_device_processes(device_sno,app_name)
                    process_select.set_options(processes)

                app_select = ui.select([],label="选择APP",on_change=_on_app_changed,with_input=True).props('dense').classes("w-full").props("dense")
                with app_select.add_slot("prepend"):
                    ui.icon("apps")
                
                process_select = ui.select([],label="选择进程").classes("w-full").props("dense")
                with process_select.add_slot("prepend"):
                    ui.icon("wysiwyg")

                with ui.row().classes("items-center w-full justify-end"):
                    def _start_profiler():
                         btn_record.props("add=loading")

                    btn_record = ui.button(icon="lens",text="开始采集",on_click=_start_profiler).props("bg-color='primary' color=red")



async def _create_deviceinfo_card():
        with ui.card().tight().style("width:100%"):
            ui.table(columns=columns,rows=rows).props("dense separator=cell bordered").classes("w-full")

            with ui.card_section().style("width:100%").style("text-align:right"):
                ui.button(icon="copy_all",on_click=lambda:ui.notification("已复制到剪贴板",position='top'))

async def _create_monitor_view():
        with ui.row().classes("size-full"):
            with ui.scroll_area().classes("flex-1 size-full p-0 min-w-96"):
                with ui.card().tight().style("width:100%"):
                    with ui.card_section():
                        ui.label('Lorem ipsum dolor sit amet, consectetur adipiscing elit, ...')



@ui.page('/android_profiler',title='Android Profier')
async def android_profier():
    AndroidProfielerService.start_scan_devices()

    Frame()

    await _create_drawer()
    await _create_monitor_view()