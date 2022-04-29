#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   effects.py
@Time    :   2022/04/27 20:09:48
@Author  :   Calros Teng 
@Version :   1.0
@Contact :   303359166@qq.com
@License :   (C)Copyright 2017-2018, Xin Yuan Studio
@Desc    :   通用特效封装到这里用工厂的方式获得
"""

# here put the import lib
from PySide6.QtWidgets import QWidget, QGraphicsDropShadowEffect, QLayout
from PySide6.QtGui import QColor
from PySide6.QtCore import QPropertyAnimation, QEasingCurve

# 动画缓存
# 因为动画对象在播放的过程中如果不引用着还是会被销毁
anim_temp = []


def set_shadow_effect(owner: QWidget):
    shadow_effect = QGraphicsDropShadowEffect(owner)
    shadow_effect.setOffset(1, 1)
    shadow_effect.setColor(QColor("#1b1e23"))
    shadow_effect.setBlurRadius(5)
    owner.setGraphicsEffect(shadow_effect)


def set_h_expand_anim(
    owner: QWidget, checked: bool, max: float, min: float
) -> QPropertyAnimation:
    anim = QPropertyAnimation(owner, b"maximumWidth")
    anim_temp.append(anim)
    anim.setStartValue(owner.maximumWidth())
    if checked:
        anim.setEndValue(max)
    else:
        anim.setEndValue(min)

    anim.setEasingCurve(QEasingCurve.InOutCubic)
    anim.setDuration(500)
    anim.start()

    def delete():
        anim_temp.remove(anim)

    # 播放完自己移除掉anim对象的引用，让其自生自灭
    anim.finished.connect(delete)
    return anim


def clear_layout(layout: QLayout | QWidget):
    """
    清空layout里的widget

    _extended_summary_

    Args:
        layout (QLayout): _description_
    """
    if isinstance(layout, QWidget):
        layout = layout.layout()

    counts = layout.count()
    for index in range(counts):
        item = layout.itemAt(index)
        layout.removeItem(item)
