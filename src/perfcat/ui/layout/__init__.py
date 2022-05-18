#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   __init__.py
@Time    :   2022/04/27 16:11:12
@Author  :   Calros Teng 
@Version :   1.0
@Contact :   303359166@qq.com
@License :   (C)Copyright 2017-2018, Xin Yuan Studio
@Desc    :   主体窗口

#todo:
[1] windows操作系统的窗口动画对无边窗口不起作用，所以放大缩小没有动画，也不能贴边触发分屏
目前还不知道怎么解决这个问题，用了win32api结果抽了
"""

# here put the import lib
import logging
import PySide6
import markdown
import textwrap
from unittest.case import doModuleCleanups

from PySide6.QtWidgets import QMainWindow, QPushButton, QWidget
from PySide6.QtCore import Qt, QPoint, QRect
from PySide6.QtGui import QMouseEvent, QHoverEvent

from perfcat.pages.home.home import Page
from perfcat.settings import settings

from . import util
from .ui_mainwindow import Ui_MainWindow

from .left_menu import LeftMenu
from .title_bar import TitleBar
from .left_column import LeftColumn


log = logging.getLogger(__name__)


class MainWindow(QMainWindow, Ui_MainWindow):

    BORDER_LIMIT = 10

    LEFT_COLUMN_MAXWIDTH = 240
    LEFT_COLUMN_MINWIDTH = 0

    CONTENT_RIGHT_MAXWIDTH = 240
    CONTENT_RIGHT_MINWIDTH = 0

    def __init__(self) -> None:
        super().__init__()
        # 初始化ui文件
        self.setupUi(self)
        self.setStyleSheet("")  # 清空qt designer里写死的样式

        # 设置flag
        # 隐藏窗体边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 缩放
        # todo
        self.installEventFilter(self)
        self._resizing = False
        self._resize_mode = None

        # 设置阴影（很淡……几乎看不见，有点感觉就行）
        util.set_shadow_effect(self)
        util.set_shadow_effect(self.setting_frame)

        # 清除掉page_stacked默认的widget
        self.page_stacked.removeWidget(self.page)
        self.page.deleteLater()  # 销毁掉

        # 添加左导航菜单
        self._setup_leftmenu()

        # 添加标题栏
        self._setup_title_bar()

        # 添加状态栏
        self._setup_status_bar()

        # 添加左面板栏
        self._setup_left_column()

    # region 页面相关
    def add_page(self, page: Page):
        """
        添加页面

        框架默认把页面的object_name和导航按钮的object_name设置成一样
        通过这种方式关联按钮和页面的切换

        Args:
            page (Page): _description_
        """
        page.setParent(self)

        icon = page.windowIcon()
        title = page.windowTitle()

        # warning：addwidget必须比add_nav_menu先调用，因为如果是第一个菜单还需要触发切换到第一个页面
        self.page_stacked.addWidget(page)

        self.left_menu.add_nav_menu(icon, title, page.objectName())

        log.debug(f"添加页面 page_name:{page.objectName()} title:{title}")

    def switch_page(self, page: Page):
        log.debug(f"切换页面到 {page.objectName()}")
        self.expand_setting_frame(False)  # 收起setting
        self.page_stacked.setCurrentWidget(page)
        # page.show()
        self.title_bar.btn_setting.setEnabled(page.setting_widget != None)

        if page.setting_widget:
            log.debug(f"页面 {page.objectName()} 有设置界面，设置 setting {page.setting_widget}")
            util.clear_layout(self.setting_container)
            # setting_widget 从setting_container里删除后parent引用失效，所以重新设置回page。
            page.setting_widget.setParent(page)
            self.setting_container.layout().addWidget(page.setting_widget)

    def _on_switch_page(self, button: QPushButton, checked):
        log.debug(f"触发切换页面 {button} {checked}")
        page_name = button.objectName()
        page: Page = self.page_stacked.findChild(Page, page_name)
        self.switch_page(page)

    # endregion

    @property
    def current_page(self) -> Page:
        return self.page_stacked.currentWidget()

    def set_about_info(self, text: str):
        """
        设置关于信息，支持markdown

        Args:
            text (str): 文本， 可以用markdown
        """
        text = textwrap.dedent(text)  # 对齐缩进
        html = markdown.markdown((text))
        self.left_column.te_about.setHtml(html)

    def setWindowFilePath(self, filePath: str) -> None:
        super().setWindowFilePath(filePath)
        self.windowTitleChanged.emit(self.windowTitle())

    def setWindowModified(self, arg__1: bool) -> None:
        super().setWindowModified(arg__1)
        self.windowTitleChanged.emit(self.windowTitle())

    def _setup_leftmenu(self):
        self.left_menu = LeftMenu(self)
        self.left_menu.setObjectName("LeftMenu")
        self.left_menu_frame.layout().addWidget(self.left_menu)

        # 添加阴影
        util.set_shadow_effect(self.left_menu_frame)

        # 导航按钮组点击的时候切换页面
        self.left_menu.nav_menu_group.buttonToggled.connect(self._on_switch_page)

        # 底部按钮组点击的时候触发展开左栏
        self.left_menu.bottom_btn_group.idToggled.connect(
            self._toggle_left_column_frame
        )

    def _setup_title_bar(self):
        # 添加标题栏
        self.title_bar = TitleBar(self)
        self.title_bar.setObjectName("TitleBar")
        self.title_bar_frame.layout().addWidget(self.title_bar)

        # 设置阴影
        util.set_shadow_effect(self.title_bar_frame)

        # 页面设置按钮
        self.title_bar.btn_setting.toggled.connect(self.expand_setting_frame)

    def _setup_status_bar(self):
        util.set_shadow_effect(self.status_bar_frame)

    def _setup_left_column(self):
        self.left_column = LeftColumn(self)
        self.left_column_frame.layout().addWidget(self.left_column)

        self.left_column.btn_close.clicked.connect(
            lambda: self.expand_left_column_frame(False)
        )

    @property
    def left_column_visible(self) -> bool:
        return self.left_column_frame.maximumWidth() > 0

    @property
    def setting_frame_visible(self) -> bool:
        return self.setting_frame.maximumWidth() > 0

    def _toggle_left_column_frame(self, id, checked: bool):

        if not self.left_column_visible:
            self.expand_left_column_frame(True)

        self.left_column.stacked.setCurrentIndex(id)
        button = self.left_menu.bottom_btn_group.button(id)
        button_text = button.text()
        self.left_column.title.setText(button_text)

    def expand_left_column_frame(self, checked: bool):
        util.set_h_expand_anim(
            self.left_column_frame,
            checked,
            self.LEFT_COLUMN_MAXWIDTH,
            self.LEFT_COLUMN_MINWIDTH,
        )
        if not checked:
            # 折叠回去了，清除掉底部互斥选项卡的选中
            self.left_menu.bottom_btn_group_reset()

    def expand_setting_frame(self, checked: bool):
        """
        展开当前页面的设置界面

        这个方法不仅仅用于信号调用，直接调用也可以展开和收起setting

        Args:
            checked (bool): _description_
        """
        util.set_h_expand_anim(
            self.setting_frame,
            checked,
            self.CONTENT_RIGHT_MAXWIDTH,
            self.CONTENT_RIGHT_MINWIDTH,
        )
        self.title_bar.btn_setting.setChecked(checked)

    def closeEvent(self, event: PySide6.QtGui.QCloseEvent) -> None:
        settings.setValue("mainwindow/geometry", self.saveGeometry())
        settings.setValue("mainwindow/state", self.saveState())
        return super().closeEvent(event)

    def showEvent(self, event: PySide6.QtGui.QShowEvent) -> None:
        geometry = settings.value("mainwindow/geometry", None)
        state = settings.value("mainwindow/state", None)
        if geometry and state:
            self.restoreGeometry(geometry)
            self.restoreState(state)
        return super().showEvent(event)

    def eventFilter(
        self, watched: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent
    ) -> bool:
        if isinstance(event, QHoverEvent) and not self._resizing:

            mouse_pos = event.pos()
            rect = self.rect()
            top_area = QRect(rect)
            top_area.setHeight(self.BORDER_LIMIT)

            bottom_area = QRect(rect)
            bottom_area.setTop(rect.top() + rect.height() - self.BORDER_LIMIT)
            bottom_area.setHeight(self.BORDER_LIMIT)

            left_area = QRect(rect)
            left_area.setWidth(self.BORDER_LIMIT)

            right_area = QRect(rect)
            right_area.setLeft(rect.left() + rect.width() - self.BORDER_LIMIT)

            on_top = top_area.contains(mouse_pos)
            on_bottom = bottom_area.contains(mouse_pos)
            on_left = left_area.contains(mouse_pos)
            on_right = right_area.contains(mouse_pos)
            on_lefttop_corner = on_top and on_left
            on_righttop_corner = on_top and on_right
            on_leftbottom_corner = on_left and on_bottom
            on_rightbottom_corner = on_right and on_bottom

            # print(on_top, on_bottom, on_left, on_right)
            if on_lefttop_corner:
                self.setCursor(Qt.CursorShape.SizeFDiagCursor)
                self._resize_mode = Qt.LeftEdge | Qt.TopEdge
            elif on_righttop_corner:
                self.setCursor(Qt.CursorShape.SizeBDiagCursor)
                self._resize_mode = Qt.RightEdge | Qt.TopEdge
            elif on_leftbottom_corner:
                self.setCursor(Qt.CursorShape.SizeBDiagCursor)
                self._resize_mode = Qt.LeftEdge | Qt.BottomEdge
            elif on_rightbottom_corner:
                self.setCursor(Qt.CursorShape.SizeFDiagCursor)
                self._resize_mode = Qt.RightEdge | Qt.BottomEdge
            elif on_top or on_bottom:
                self.setCursor(Qt.SizeVerCursor)
                if on_top:
                    self._resize_mode = Qt.TopEdge
                elif on_bottom:
                    self._resize_mode = Qt.BottomEdge
            elif on_left or on_right:
                self.setCursor(Qt.SizeHorCursor)
                if on_left:
                    self._resize_mode = Qt.LeftEdge
                elif on_right:
                    self._resize_mode = Qt.RightEdge
            else:
                self.setCursor(Qt.ArrowCursor)
                self._resize_mode = None

        return super().eventFilter(watched, event)

    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:

        self._resizing = True
        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        self._resizing = False
        return super().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:

        if self._resizing:

            if self._resize_mode:
                global_pos = event.globalPos()
                geometry = self.geometry()
                if self._resize_mode == Qt.TopEdge:
                    geometry.setTop(global_pos.y())
                elif self._resize_mode == Qt.BottomEdge:
                    geometry.setBottom(global_pos.y())
                elif self._resize_mode == Qt.LeftEdge:
                    geometry.setLeft(global_pos.x())
                elif self._resize_mode == Qt.RightEdge:
                    geometry.setRight(global_pos.x())
                elif self._resize_mode == Qt.TopEdge | Qt.LeftEdge:
                    geometry.setTopLeft(global_pos)
                elif self._resize_mode == Qt.TopEdge | Qt.RightEdge:
                    geometry.setTopRight(global_pos)
                elif self._resize_mode == Qt.BottomEdge | Qt.LeftEdge:
                    geometry.setBottomLeft(global_pos)
                elif self._resize_mode == Qt.BottomEdge | Qt.RightEdge:
                    geometry.setBottomRight(global_pos)

                if (
                    geometry.width() > self.minimumWidth()
                    and geometry.height() > self.minimumHeight()
                ):
                    self.setGeometry(geometry)

        return super().mouseMoveEvent(event)
