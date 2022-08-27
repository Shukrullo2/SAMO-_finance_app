from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget, QLineEdit)
from PySide6 import QtGui
from functools import partial

"""The app is structured according to MVP model.
Below is the View part"""
class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SAMO hisoblagich")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("samo.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.setWindowIcon(icon)
        self.setWindowIcon(icon)
        self.resize(800, 626)
        self.centralwidget = QWidget()
        self.centralwidget.setObjectName(u"centralwidget")
        self.sadaqa = QLineEdit(self.centralwidget)
        self.sadaqa.setObjectName(u"sadaqa")
        self.sadaqa.setGeometry(QRect(250, 200, 121, 31))
        self.otaona = QLineEdit(self.centralwidget)
        self.otaona.setObjectName(u"otaona")
        self.otaona.setGeometry(QRect(250, 140, 121, 31))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(120, 100, 21, 281))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(130, 150, 121, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(130, 210, 121, 16))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.oilaviyByudjet = QLineEdit(self.centralwidget)
        self.oilaviyByudjet.setObjectName(u"oilaviyByudjet")
        self.oilaviyByudjet.setGeometry(QRect(250, 360, 121, 31))
        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(130, 370, 121, 16))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.kongil = QLineEdit(self.centralwidget)
        self.kongil.setObjectName(u"kongil")
        self.kongil.setGeometry(QRect(510, 240, 121, 31))
        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(390, 250, 121, 16))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.kelajak = QLineEdit(self.centralwidget)
        self.kelajak.setObjectName(u"kelajak")
        self.kelajak.setGeometry(QRect(510, 300, 121, 31))
        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(390, 310, 121, 16))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.oylik = QLineEdit(self.centralwidget)
        self.oylik.setObjectName(u"oylik")
        self.oylik.setGeometry(QRect(510, 360, 121, 31))
        self.line_7 = QFrame(self.centralwidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(390, 370, 121, 16))
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.line_9 = QFrame(self.centralwidget)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(380, 260, 21, 121))
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)
        self.line_10 = QFrame(self.centralwidget)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setGeometry(QRect(280, 370, 121, 16))
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 120, 63, 20))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(270, 180, 63, 20))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(530, 220, 91, 20))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(530, 280, 63, 20))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(520, 340, 111, 20))
        self.line_11 = QFrame(self.centralwidget)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setGeometry(QRect(560, 390, 21, 61))
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)
        self.line_8 = QFrame(self.centralwidget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(510, 440, 121, 16))
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)
        self.shaxsiy = QLineEdit(self.centralwidget)
        self.shaxsiy.setObjectName(u"shaxsiy")
        self.shaxsiy.setGeometry(QRect(630, 430, 121, 31))
        self.kompaniya = QLineEdit(self.centralwidget)
        self.kompaniya.setObjectName(u"kompaniya")
        self.kompaniya.setGeometry(QRect(390, 430, 121, 31))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(400, 410, 111, 20))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(640, 410, 111, 20))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(260, 340, 111, 20))
        self.orzu = QLineEdit(self.centralwidget)
        self.orzu.setObjectName(u"orzu")
        self.orzu.setGeometry(QRect(510, 500, 121, 31))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(520, 480, 111, 20))
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(280, 480, 111, 20))
        self.line_12 = QFrame(self.centralwidget)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setGeometry(QRect(390, 510, 121, 16))
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)
        self.kapital = QLineEdit(self.centralwidget)
        self.kapital.setObjectName(u"kapital")
        self.kapital.setGeometry(QRect(270, 500, 121, 31))
        self.line_13 = QFrame(self.centralwidget)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setGeometry(QRect(440, 460, 21, 61))
        self.line_13.setFrameShape(QFrame.VLine)
        self.line_13.setFrameShadow(QFrame.Sunken)
        self.kirim = QLineEdit(self.centralwidget)
        self.kirim.setObjectName(u"kirim")
        self.kirim.setGeometry(QRect(70, 70, 121, 31))
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(100, 50, 63, 20))
        self.tozala = QPushButton(self.centralwidget)
        self.tozala.setObjectName(u"tozala")
        self.tozala.setGeometry(QRect(660, 110, 83, 29))
        self.hisobla = QPushButton(self.centralwidget)
        self.hisobla.setObjectName(u"hisobla")
        self.hisobla.setGeometry(QRect(660, 60, 83, 29))


        self.setCentralWidget(self.centralwidget)
        self.line_10.raise_()
        self.sadaqa.raise_()
        self.otaona.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.oilaviyByudjet.raise_()
        self.line_4.raise_()
        self.kongil.raise_()
        self.line_5.raise_()
        self.kelajak.raise_()
        self.line_6.raise_()
        self.oylik.raise_()
        self.line_7.raise_()
        self.line_9.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.line_11.raise_()
        self.line_8.raise_()
        self.shaxsiy.raise_()
        self.kompaniya.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.orzu.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.line_12.raise_()
        self.kapital.raise_()
        self.line_13.raise_()
        self.kirim.raise_()
        self.label_11.raise_()
        self.tozala.raise_()
        self.hisobla.raise_()
        self.menubar = QMenuBar()
        self.menubar = QMenuBar()
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar()
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        # QMetaObject.connectSlotsByName()

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Hisoblagich", u"Hisoblagich", None))
        self.label.setText(QCoreApplication.translate("Hisoblagich", u"Ota-ona", None))
        self.label_2.setText(QCoreApplication.translate("Hisoblagich", u"Sadaqa", None))
        self.label_3.setText(QCoreApplication.translate("Hisoblagich", u"Ko'ngil ochish", None))
        self.label_4.setText(QCoreApplication.translate("Hisoblagich", u"Kelajak", None))
        self.label_5.setText(QCoreApplication.translate("Hisoblagich", u"Oylik Daromad", None))
        self.label_6.setText(QCoreApplication.translate("Hisoblagich", u"Kompaniya hisobi", None))
        self.label_7.setText(QCoreApplication.translate("Hisoblagich", u"Shaxsiy hisob", None))
        self.label_8.setText(QCoreApplication.translate("Hisoblagich", u"Oilaviy Byudjet", None))
        self.label_9.setText(QCoreApplication.translate("Hisoblagich", u"Orzu", None))
        self.label_10.setText(QCoreApplication.translate("Hisoblagich", u"Kapital", None))
        self.label_11.setText(QCoreApplication.translate("Hisoblagich", u"Asosiy kirim", None))
        self.tozala.setText(QCoreApplication.translate("Hisoblagich", u"Tozala", None))
        self.hisobla.setText(QCoreApplication.translate("Hisoblagich", u"Hisobla", None))

"""Model part of the app"""
class evaluate():
    def __init__(self, view):
        self._view = view
    def calcFromKirim(self, valueKirim = '1'):
        if valueKirim == "1":
            valueKirim = float(self._view.kirim.text())
        self._view.otaona.setText(str(valueKirim*0.1))
        self._view.sadaqa.setText(str(valueKirim * 0.025))
        self._view.oilaviyByudjet.setText(str(valueKirim * 0.875))
        valueOila = (valueKirim * 0.875)
        self._view.kirim.setText(str(valueOila / 0.875))
        self._view.kongil.setText(str(valueOila * 0.10))
        self._view.kelajak.setText(str(valueOila * 0.10))
        self._view.oylik.setText(str(valueOila * 0.8))
        valueOylik = valueOila*0.8
        self._view.shaxsiy.setText(str(valueOylik * 0.45))
        self._view.kompaniya.setText(str(valueOylik*0.55))
        valueKompaniya = valueOylik*0.55
        self._view.kapital.setText(str(valueKompaniya * 0.80))
        self._view.orzu.setText(str(valueKompaniya * 0.20))
    def calcFromOtaona(self):
        valueOtaona = str(self._view.otaona.text())
        valueKirim = str(float(valueOtaona)*10)
        self.calcFromKirim(valueKirim=valueKirim)
    def calcFromSadaqa(self):
        valueSadaqa = self._view.sadaqa.text()
        valueKirim = float(valueSadaqa)*40
        self.calcFromKirim(valueKirim=valueKirim)
    def calcFromOilaviyByudjet(self, valueOilaviyByudjet = 1):
        if valueOilaviyByudjet == 1:
            valueOilaviyByudjet = float(self._view.oilaviyByudjet.text())
        valueKirim = valueOilaviyByudjet / 0.875
        self.calcFromKirim(valueKirim=valueKirim)
    def calcFromKongil(self):
        valueKongil = float(self._view.kongil.text())
        valueOilaviyByudjet = valueKongil * 10
        self.calcFromOilaviyByudjet(valueOilaviyByudjet=valueOilaviyByudjet)
    def calcFromKelajak(self):
        valueKelajak = float(self._view.kelajak.text())
        valueOilaviyByudjet = valueKelajak * 10
        self.calcFromOilaviyByudjet(valueOilaviyByudjet=valueOilaviyByudjet)
    def calcFromOylik(self, valueOylik = 1):
        if valueOylik == 1:
            valueOylik = float(self._view.oylik.text())
        valueOilaviyByudjet = valueOylik / 0.8
        self.calcFromOilaviyByudjet(valueOilaviyByudjet=valueOilaviyByudjet)
    def calcFromShaxsiy(self):
        valueShaxsiy = float(self._view.shaxsiy.text())
        valueOylik = valueShaxsiy / 0.45
        self.calcFromOylik(valueOylik=valueOylik)
    def calcFromKompaniya(self, valueKompaniya = 1):
        if valueKompaniya == 1:
            valueKompaniya = float(self._view.kompaniya.text())
        valueOylik = valueKompaniya / 0.55
        self.calcFromOylik(valueOylik=valueOylik)
    def calcFromKapital(self):
        valueKapital = float(self._view.kapital.text())
        valueKompaniya = valueKapital / 0.8
        self.calcFromKompaniya(valueKompaniya=valueKompaniya)
    def calcFromOrzu(self):
        valueOrzu = float(self._view.orzu.text())
        valueKompaniya = valueOrzu / 0.2
        self.calcFromKompaniya(valueKompaniya=valueKompaniya)
    def clearAll(self):
        list = [self._view.kirim,self._view.otaona,self._view.sadaqa,self._view.oilaviyByudjet,self._view.kongil,self._view.kelajak,self._view.oylik,self._view.kompaniya,self._view.shaxsiy,self._view.kapital,self._view.orzu]
        for item in list:
            item.setText('')

    def _hisoblaButton(self):
        list = [self._view.kirim, self._view.otaona, self._view.sadaqa, self._view.oilaviyByudjet, self._view.kongil,
                self._view.kelajak, self._view.oylik, self._view.kompaniya, self._view.shaxsiy, self._view.kapital,
                self._view.orzu]
        funcs = [self.calcFromKirim, self.calcFromOtaona, self.calcFromSadaqa, self.calcFromOilaviyByudjet, self.calcFromKongil, self.calcFromKelajak, self.calcFromOylik, self.calcFromKompaniya,
                 self.calcFromShaxsiy, self.calcFromKapital, self.calcFromOrzu]
        for i, item in enumerate(list):
            if item.text() != '':
                funcs[i]()
                break
        for item in list:
            item.setText('%.2f' % float(item.text() ))

"""Here is the Controller"""
class Ctrlr():
    def __init__(self, model, view):
        self._model = model
        self._view = view
        view.tozala.clicked.connect(self._model.clearAll)
        view.hisobla.clicked.connect(partial(self._model._hisoblaButton))
        list = [self._view.kirim, self._view.otaona, self._view.sadaqa, self._view.oilaviyByudjet, self._view.kongil,
                self._view.kelajak, self._view.oylik, self._view.kompaniya, self._view.shaxsiy, self._view.kapital,
                self._view.orzu]
        for item in list:
            item.returnPressed.connect(partial(self._model._hisoblaButton))


#create the application instance
app = QApplication([])
#Creating the instance of View
window = Ui_MainWindow()
# Creating the Controller instance
model = evaluate(view=window)
window.show()
#Connecting View and Model through controller class
Ctrlr(model=model, view=window)
app.exec()


