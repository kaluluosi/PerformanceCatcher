from nicegui import ui
from fastapi import Request
from perfcat.components.layout import frame



@ui.page('/android_profiler',title='Android Profier')
async def android_profier(request: Request):
    
    with frame():
        ui.label('Android Profier')