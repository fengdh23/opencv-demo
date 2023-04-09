# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'check_img_color.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.open_camera = QPushButton(self.centralwidget)
        self.open_camera.setObjectName(u"open_camera")
        self.open_camera.setGeometry(QRect(610, 70, 75, 23))
        self.close_camera = QPushButton(self.centralwidget)
        self.close_camera.setObjectName(u"close_camera")
        self.close_camera.setGeometry(QRect(610, 180, 75, 23))
        self.check_result = QLabel(self.centralwidget)
        self.check_result.setObjectName(u"check_result")
        self.check_result.setGeometry(QRect(590, 400, 121, 51))
        self.capture = QPushButton(self.centralwidget)
        self.capture.setObjectName(u"capture")
        self.capture.setGeometry(QRect(610, 130, 75, 23))
        self.select_file = QPushButton(self.centralwidget)
        self.select_file.setObjectName(u"select_file")
        self.select_file.setGeometry(QRect(610, 250, 75, 23))
        self.show_camera = QLabel(self.centralwidget)
        self.show_camera.setObjectName(u"show_camera")
        self.show_camera.setGeometry(QRect(160, 70, 281, 191))
        self.show_image = QLabel(self.centralwidget)
        self.show_image.setObjectName(u"show_image")
        self.show_image.setGeometry(QRect(150, 310, 281, 191))
        self.checkColor = QPushButton(self.centralwidget)
        self.checkColor.setObjectName(u"checkColor")
        self.checkColor.setGeometry(QRect(610, 310, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.open_camera.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6444\u50cf\u5934", None))
        self.close_camera.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u6444\u50cf\u5934", None))
        self.check_result.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u7ed3\u679c", None))
        self.capture.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u7167", None))
        self.select_file.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u56fe\u7247", None))
        self.show_camera.setText(QCoreApplication.translate("MainWindow", u"\u6444\u50cf\u5934\u9884\u89c8", None))
        self.show_image.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u9884\u89c8", None))
        self.checkColor.setText(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b\u56fe\u7247", None))
    # retranslateUi

