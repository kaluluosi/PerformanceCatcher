"""
author:        kaluluosi111 <kaluluosi@gmail.com>
date:          2025-06-21 20:31:04
Copyright © Kaluluosi All rights reserved
"""

from nicegui import app, ui
from nicegui.observables import ObservableDict

from contextlib import contextmanager

from pydantic import BaseModel, Field, RootModel


class SerieData(BaseModel):
    name: str
    type: str = "line"
    data: list[float] = Field(default_factory=list)


Series = RootModel[list[SerieData]]


class MonitorTabPanel(ui.tab_panel):
    def __init__(self, name: str | ui.tab) -> None:
        super().__init__(name)
        self.classes("w-full")


class ControlCard(ui.card):
    def __init__(self) -> None:
        super().__init__()
        self.tight()
        self.classes("w-full")

    @contextmanager
    def session(self):
        with ui.card_section().classes("w-full"):
            with ui.row().classes("items-center w-full"):
                yield

    @contextmanager
    def actions(self):
        with ui.card_actions().classes("w-full"):
            yield


class Drawer(ui.drawer):
    def __init__(self) -> None:
        super().__init__(side="right", value=True, elevated=True)
        self.bind_value(app.storage.general, "android_profiler_drawer_expand")
        self.classes("p-0")
        self.props("width=400")

        with ui.page_sticky(position="top-right", y_offset=100).style("z-index:2000"):
            self.btn_expand = ui.button(
                icon="arrow_left", on_click=lambda: self.toggle()
            )
            self.btn_expand.classes("pl-2 pr-2 pt-8 pb-8 w-1")
            self.btn_expand.style("border-radius:3px 0px 0px 3px;")

    @contextmanager
    def create_tabs(self):
        self.tabs = ui.tabs()
        with self.tabs:
            yield

    @contextmanager
    def create_tab_panels(self):
        self.tab_panels = ui.tab_panels(self.tabs).classes("w-full")
        with self.tab_panels:
            yield


class MonitorCard(ui.card):
    title: str = "Monitor"

    def __init__(self) -> None:
        super().__init__()
        self.classes("w-full")

        self._series: list[SerieData] = []

        with self:
            with ui.card_section().classes("w-full"):
                self.label_title = ui.label(self.title)
                ui.separator()

            with self:
                self.chart = ui.echart(
                    {
                        "legend": {"data": [], "orient": "vertical", "left": 10},
                        "grid": {
                            "left": "100px",
                            "right": "4%",
                            "top": "3%",
                            "bottom": "10%",
                            "containLabel": True,
                        },
                        "xAxis": {"type": "category"},
                        "yAxis": {"type": "value"},
                        "series": [],
                        "axisPointer": {
                            "link": {"xAxisIndex": "all"},
                            "label": {"backgroundColor": "#777"},
                        },
                        "tooltip": {
                            "trigger": "axis",
                            "axisPointer": {"type": "cross"},
                            "backgroundColor": "rgba(255, 255, 255, 0.8)",
                            "position": "js:function (pos, params, el, elRect, size) { var obj = { top: 10 }; obj[['left', 'right'][+(pos[0] < size.viewSize[0] / 2)]] = 30; return obj; }",
                            "extraCssText": "width: 170px",
                        },
                        "dataZoom": [
                            {
                                "type": "inside",
                                "start": 0,
                                "end": 100,
                            },
                            {
                                "type": "slider",
                                "show": False,
                                "start": 0,
                                "end": 100,
                            }
                        ],
                    }
                )

                self.datazoom = ui.range(min=0,max=100,value={'min':0,'max':100},step=1)
                self.datazoom.bind_value(app.storage.general, "android_profiler_datazoom")

    @contextmanager
    def session(self):
        with ui.card_section().classes("w-full"):
            yield

    def create_serie(self, name: str, type: str = "line"):
        serie = SerieData(name=name, type=type, data=[])
        self._series.append(serie)

    def _add_point(self, serie_name: str, value: float, type: str = "line"):
        if serie_name not in [serie.name for serie in self._series]:
            self.create_serie(serie_name, type)
        
        for serie in self._series:
            if serie.name == serie_name:
                serie.data.append(value)
                return

    def update_chart(self):
        self.chart.options["series"] = Series(self._series).model_dump()
        self.chart.options["legend"]["data"] = [serie.name for serie in self._series]
        self.chart.options['dataZoom'][0]['start'] = self.datazoom.value['min']
        self.chart.options['dataZoom'][0]['end'] = self.datazoom.value['max']
        self.chart.update()

    def sample(self):
        raise NotImplementedError
