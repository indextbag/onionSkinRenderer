# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Personal Work\2017\OnionSkinRenderer\onionSkinRenderer\2016\onionSkinRenderer\onionSkinRendererFrameWidget.ui'
#
# Created: Wed Feb 21 16:52:45 2018
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_onionSkinFrame_layout(object):
    def setupUi(self, onionSkinFrame_layout):
        onionSkinFrame_layout.setObjectName("onionSkinFrame_layout")
        onionSkinFrame_layout.resize(267, 28)
        onionSkinFrame_layout.setMinimumSize(QtCore.QSize(0, 16))
        onionSkinFrame_layout.setStyleSheet("QWidget::border: 1px solid rgb(18, 18, 18)")
        self.frame_widget_layout = QtGui.QHBoxLayout(onionSkinFrame_layout)
        self.frame_widget_layout.setContentsMargins(4, 0, 4, 0)
        self.frame_widget_layout.setObjectName("frame_widget_layout")
        self.frame_number = QtGui.QLabel(onionSkinFrame_layout)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_number.sizePolicy().hasHeightForWidth())
        self.frame_number.setSizePolicy(sizePolicy)
        self.frame_number.setMinimumSize(QtCore.QSize(24, 0))
        self.frame_number.setStyleSheet("font: 10pt;\n"
"padding-right: 5px;\n"
"padding-left: 5px;")
        self.frame_number.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.frame_number.setMargin(0)
        self.frame_number.setIndent(0)
        self.frame_number.setObjectName("frame_number")
        self.frame_widget_layout.addWidget(self.frame_number)
        self.frame_opacity_slider = QtGui.QSlider(onionSkinFrame_layout)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_opacity_slider.sizePolicy().hasHeightForWidth())
        self.frame_opacity_slider.setSizePolicy(sizePolicy)
        self.frame_opacity_slider.setMinimumSize(QtCore.QSize(30, 0))
        self.frame_opacity_slider.setStyleSheet("QSlider{\n"
"border: 1px solid rgb(20, 20, 20);\n"
"margin: 4px;\n"
"background: rgb(150, 150, 150);\n"
"}\n"
"QSlider::handle{\n"
"height: 8px;\n"
"background: rgb(50, 50, 50);\n"
"border: 1px solid rgb(20, 20, 20);\n"
"margin: -4px -4px;\n"
"}\n"
"QSlider::groove{\n"
"background: grey;\n"
"}\n"
"QSlider::sub-page{\n"
"background: rgb(75, 75, 75);\n"
"}\n"
"QSlider::add-page{\n"
"background: rgb(150, 150, 150);\n"
"}")
        self.frame_opacity_slider.setMaximum(100)
        self.frame_opacity_slider.setProperty("value", 50)
        self.frame_opacity_slider.setOrientation(QtCore.Qt.Horizontal)
        self.frame_opacity_slider.setObjectName("frame_opacity_slider")
        self.frame_widget_layout.addWidget(self.frame_opacity_slider)
        self.frame_visibility_btn = QtGui.QPushButton(onionSkinFrame_layout)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_visibility_btn.sizePolicy().hasHeightForWidth())
        self.frame_visibility_btn.setSizePolicy(sizePolicy)
        self.frame_visibility_btn.setMinimumSize(QtCore.QSize(16, 16))
        self.frame_visibility_btn.setMaximumSize(QtCore.QSize(16, 16))
        self.frame_visibility_btn.setCheckable(True)
        self.frame_visibility_btn.setObjectName("frame_visibility_btn")
        self.frame_widget_layout.addWidget(self.frame_visibility_btn)

        self.retranslateUi(onionSkinFrame_layout)
        QtCore.QMetaObject.connectSlotsByName(onionSkinFrame_layout)

    def retranslateUi(self, onionSkinFrame_layout):
        onionSkinFrame_layout.setWindowTitle(QtGui.QApplication.translate("onionSkinFrame_layout", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.frame_number.setText(QtGui.QApplication.translate("onionSkinFrame_layout", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.frame_visibility_btn.setText(QtGui.QApplication.translate("onionSkinFrame_layout", "v", None, QtGui.QApplication.UnicodeUTF8))

