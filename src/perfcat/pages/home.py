from nicegui import ui,app
from fastapi import Request
from perfcat.components.layout import Frame


@ui.page("/",title="主页")
async def home(request:Request):
    Frame()
