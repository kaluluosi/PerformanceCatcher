from nicegui import ui,app
from fastapi import Request
from perfcat.components.layout import frame


@ui.page("/",title="主页")
async def home(request:Request):
    
    with frame():
        pass