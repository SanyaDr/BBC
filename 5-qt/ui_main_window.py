# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QTextBrowser, QWidget)

class Ui_MyMainWindow(object):
    def setupUi(self, MyMainWindow):
        if not MyMainWindow.objectName():
            MyMainWindow.setObjectName(u"MyMainWindow")
        MyMainWindow.resize(395, 513)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MyMainWindow.sizePolicy().hasHeightForWidth())
        MyMainWindow.setSizePolicy(sizePolicy)
        self.plainTextEdit = QPlainTextEdit(MyMainWindow)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(10, 10, 371, 151))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        self.plainTextEdit.setPalette(palette)
        self.pushButton_2 = QPushButton(MyMainWindow)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(90, 170, 191, 31))
        self.label = QLabel(MyMainWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 230, 71, 21))
        self.textBrowser = QTextBrowser(MyMainWindow)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(75, 210, 311, 291))
        palette1 = QPalette()
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        self.textBrowser.setPalette(palette1)

        self.retranslateUi(MyMainWindow)

        QMetaObject.connectSlotsByName(MyMainWindow)
    # setupUi

    def retranslateUi(self, MyMainWindow):
        MyMainWindow.setWindowTitle(QCoreApplication.translate("MyMainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0437 \u0442\u0435\u043a\u0441\u0442\u0430", None))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MyMainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442", None))
        self.pushButton_2.setText(QCoreApplication.translate("MyMainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0437", None))
        self.label.setText(QCoreApplication.translate("MyMainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442:", None))
    # retranslateUi

