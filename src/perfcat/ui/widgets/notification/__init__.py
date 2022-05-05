import PySide6
import logging

from typing import Optional
from PySide6.QtWidgets import QWidget,QGraphicsOpacityEffect
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QTimer,QParallelAnimationGroup,Qt

import perfcat

from .ui_notification import Ui_Notification
from perfcat.ui.constant import ButtonStyle,Color

log = logging.getLogger(__name__)

class Notification(QWidget, Ui_Notification):
    
    count = 1
    
    def __init__(self, parent: Optional[QWidget] = None, msg:str="消息提示", style:ButtonStyle=ButtonStyle.warning) -> None:
        parent = parent.window()
        super().__init__(parent)
        self.setupUi(self)

        self.setStyleSheet("")
        
        self.move(
            parent.rect().right()-self.width(),
            parent.rect().bottom()-self.height()*Notification.count
        )
        
        Notification.count+=1
        
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
        
        self.btn_msg.setText(msg)
        self.btn_msg.setStyleSheet(f'background-color:{Color[style.value]};')
        

        width_animation = QPropertyAnimation(self.frame, b'maximumWidth')
        width_animation.setStartValue(0)
        width_animation.setEndValue(self.frame.maximumWidth())
        width_animation.setEasingCurve(QEasingCurve.InOutBounce)
        width_animation.setDuration(200)
        self.animation = width_animation
        
        self.destroyed.connect(lambda : self._on_destroyed())

        
    def showEvent(self, event: PySide6.QtGui.QShowEvent) -> None:
        
        self.animation.setDirection(QPropertyAnimation.Forward)
        self.animation.start()
        
        # 定时销毁
        self.auto_destory_timer = QTimer(self)
        self.auto_destory_timer.setInterval(1000)
        self.auto_destory_timer.setSingleShot(True)
        self.auto_destory_timer.timeout.connect(lambda :self.destroy())
        self.auto_destory_timer.start()
        
        return super().showEvent(event)
    
    def destroy(self, destroyWindow: bool = True, destroySubWindows: bool = True) -> None:
        self.animation.setDirection(QPropertyAnimation.Backward)
        self.animation.start()
        log.debug("开始销毁动画")
        self.animation.finished.connect(
            self._on_deleted
        )
        return super().destroy()
    
    def _on_destroyed(self):
        log.debug("减少Notification.count的计数")
        Notification.count -= 1
    
    def _on_deleted(self):
        self.deleteLater()
        log.debug("调用deletelater")