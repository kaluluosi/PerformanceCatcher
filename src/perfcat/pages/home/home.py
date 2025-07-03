import datetime
import json
import os
from nicegui import ui
from fastapi.responses import RedirectResponse
from perfcat.components.layout import Page
from perfcat.services import RecordService


@ui.page("/")
def index():
    return RedirectResponse(url="/home")


class HomePage(Page):
    def __init__(self) -> None:
        super().__init__("/home", title="主页")

    async def render(self):
        columns = [
            {"name": "name", "label": "日志名称", "field": "name", "align": "left"},
            {"name": "model_name", "label": "测试机名", "field": "model_name"},
            {"name": "package_name", "label": "包名", "field": "package_name"},
            {"name": "process", "label": "进程名", "field": "process"},
            {
                "name": "created_at",
                "label": "创建时间",
                "field": "created_at",
                "sortable": True,
                "sortOrder": "da",
            },
            {"name": "actions", "label": "操作", "field": "actions", "align": "center"},
        ]

        rows = self.load_record_data()
        with (
            ui.table(
                columns=columns,
                rows=rows,
                pagination={
                    "rowsPerPage": 50,
                    "sortBy": "created_at",
                    "descending": True,
                },
            )
            .classes("w-full h-full")
            .props("separator=cell bordered striped hoverable") as self.table
        ):
            self.table.add_slot(
                "body-cell-actions",
                """
                <q-td :props="props">
                    <q-btn @click="$parent.$emit('action_preview', props.row)" icon="preview" flat />
                    <q-btn @click="$parent.$emit('action_delete', props.row)" icon="delete" flat />
                </q-td>
            """,
            )
            self.table.on(
                "action_preview",
                lambda row: ui.navigate.to(f"/home/report/{row.args['name']}"),
            )
            self.table.on("action_delete", lambda row: None)

    def load_record_data(self):
        files = RecordService.record_files()

        datas = []
        for file in files:
            with open(f"records/{file}", "r",encoding="utf-8") as f:
                info = json.loads(f.readline().strip())
                create_at = os.stat(f"records/{file}").st_ctime
                datas.append(
                    {
                        "name": file,
                        "model_name": info.get("model", "未知"),
                        "package_name": info.get("app", "未知"),
                        "process": info.get("process", "未知"),
                        "created_at": datetime.datetime.fromtimestamp(
                            create_at
                        ).strftime("%Y-%m-%d %H:%M:%S"),
                    }
                )

        return datas


HomePage()
