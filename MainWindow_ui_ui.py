# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QMainWindow,
    QMenuBar, QSizePolicy, QStatusBar, QTabWidget,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(783, 679)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 761, 631))
        self.Loaddf = QWidget()
        self.Loaddf.setObjectName(u"Loaddf")
        self.Table_info_groupbox = QGroupBox(self.Loaddf)
        self.Table_info_groupbox.setObjectName(u"Table_info_groupbox")
        self.Table_info_groupbox.setGeometry(QRect(10, 10, 351, 581))
        self.label = QLabel(self.Table_info_groupbox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 49, 16))
        self.Table_feat_groupbox = QGroupBox(self.Loaddf)
        self.Table_feat_groupbox.setObjectName(u"Table_feat_groupbox")
        self.Table_feat_groupbox.setGeometry(QRect(370, 10, 371, 591))
        self.tabWidget.addTab(self.Loaddf, "")
        self.Managedf = QWidget()
        self.Managedf.setObjectName(u"Managedf")
        self.groupBox = QGroupBox(self.Managedf)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 10, 301, 501))
        self.groupBox_2 = QGroupBox(self.Managedf)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(330, 10, 301, 501))
        self.tabWidget.addTab(self.Managedf, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 783, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Table_info_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"Table info", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Table_feat_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"Features", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Loaddf), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Managedf), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi

