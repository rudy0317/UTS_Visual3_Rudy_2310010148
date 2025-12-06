# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'instansi_form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_InstansiForm(object):
    def setupUi(self, InstansiForm):
        if not InstansiForm.objectName():
            InstansiForm.setObjectName(u"InstansiForm")
        InstansiForm.resize(800, 600)
        self.verticalLayout = QVBoxLayout(InstansiForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelTitle = QLabel(InstansiForm)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setStyleSheet(u"font-size:20px; font-weight:bold;")
        self.labelTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.labelTitle)

        self.labelUserAktif = QLabel(InstansiForm)
        self.labelUserAktif.setObjectName(u"labelUserAktif")
        self.labelUserAktif.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.labelUserAktif)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.labelNamaInstansi = QLabel(InstansiForm)
        self.labelNamaInstansi.setObjectName(u"labelNamaInstansi")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelNamaInstansi)

        self.input_nama_instansi = QLineEdit(InstansiForm)
        self.input_nama_instansi.setObjectName(u"input_nama_instansi")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.input_nama_instansi)

        self.labelAlamat = QLabel(InstansiForm)
        self.labelAlamat.setObjectName(u"labelAlamat")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelAlamat)

        self.input_alamat = QTextEdit(InstansiForm)
        self.input_alamat.setObjectName(u"input_alamat")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.input_alamat)

        self.labelKontak = QLabel(InstansiForm)
        self.labelKontak.setObjectName(u"labelKontak")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelKontak)

        self.input_kontak = QLineEdit(InstansiForm)
        self.input_kontak.setObjectName(u"input_kontak")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.input_kontak)

        self.labelAdmin = QLabel(InstansiForm)
        self.labelAdmin.setObjectName(u"labelAdmin")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.labelAdmin)

        self.combo_admin = QComboBox(InstansiForm)
        self.combo_admin.setObjectName(u"combo_admin")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.combo_admin)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnSimpan = QPushButton(InstansiForm)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.buttonLayout.addWidget(self.btnSimpan)

        self.btnUbah = QPushButton(InstansiForm)
        self.btnUbah.setObjectName(u"btnUbah")

        self.buttonLayout.addWidget(self.btnUbah)

        self.btnHapus = QPushButton(InstansiForm)
        self.btnHapus.setObjectName(u"btnHapus")

        self.buttonLayout.addWidget(self.btnHapus)

        self.btnBersih = QPushButton(InstansiForm)
        self.btnBersih.setObjectName(u"btnBersih")

        self.buttonLayout.addWidget(self.btnBersih)

        self.btnPrint = QPushButton(InstansiForm)
        self.btnPrint.setObjectName(u"btnPrint")

        self.buttonLayout.addWidget(self.btnPrint)


        self.verticalLayout.addLayout(self.buttonLayout)

        self.input_cari = QLineEdit(InstansiForm)
        self.input_cari.setObjectName(u"input_cari")

        self.verticalLayout.addWidget(self.input_cari)

        self.tableInstansi = QTableWidget(InstansiForm)
        if (self.tableInstansi.columnCount() < 5):
            self.tableInstansi.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableInstansi.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableInstansi.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableInstansi.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableInstansi.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableInstansi.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableInstansi.setObjectName(u"tableInstansi")

        self.verticalLayout.addWidget(self.tableInstansi)


        self.retranslateUi(InstansiForm)

        QMetaObject.connectSlotsByName(InstansiForm)
    # setupUi

    def retranslateUi(self, InstansiForm):
        InstansiForm.setWindowTitle(QCoreApplication.translate("InstansiForm", u"Form Instansi", None))
        self.labelTitle.setText(QCoreApplication.translate("InstansiForm", u"Manajemen Data Instansi", None))
        self.labelUserAktif.setText(QCoreApplication.translate("InstansiForm", u"User Aktif: -", None))
        self.labelNamaInstansi.setText(QCoreApplication.translate("InstansiForm", u"Nama Instansi", None))
        self.labelAlamat.setText(QCoreApplication.translate("InstansiForm", u"Alamat", None))
        self.labelKontak.setText(QCoreApplication.translate("InstansiForm", u"Kontak", None))
        self.labelAdmin.setText(QCoreApplication.translate("InstansiForm", u"Admin", None))
        self.btnSimpan.setText(QCoreApplication.translate("InstansiForm", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("InstansiForm", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("InstansiForm", u"Hapus", None))
        self.btnBersih.setText(QCoreApplication.translate("InstansiForm", u"Bersih", None))
        self.btnPrint.setText(QCoreApplication.translate("InstansiForm", u"Print", None))
        self.input_cari.setPlaceholderText(QCoreApplication.translate("InstansiForm", u"Cari berdasarkan nama instansi", None))
        ___qtablewidgetitem = self.tableInstansi.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("InstansiForm", u"ID Instansi", None));
        ___qtablewidgetitem1 = self.tableInstansi.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("InstansiForm", u"Nama Instansi", None));
        ___qtablewidgetitem2 = self.tableInstansi.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("InstansiForm", u"Alamat", None));
        ___qtablewidgetitem3 = self.tableInstansi.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("InstansiForm", u"Kontak", None));
        ___qtablewidgetitem4 = self.tableInstansi.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("InstansiForm", u"Admin", None));
    # retranslateUi

