from nicegui import ui,app
from perfcat.components.layout import Frame
from perfcat.services.android_profiler_service import AndroidProfielerService


@ui.page("/",title="主页")
async def home():
    Frame()