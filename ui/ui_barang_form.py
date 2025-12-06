# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'barang_form.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFormLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_BarangForm(object):
    def setupUi(self, BarangForm):
        if not BarangForm.objectName():
            BarangForm.setObjectName(u"BarangForm")
        BarangForm.resize(800, 600)
        self.verticalLayout = QVBoxLayout(BarangForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelTitle = QLabel(BarangForm)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setStyleSheet(u"font-size:20px; font-weight:bold;")
        self.labelTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.labelTitle)

        self.labelUserAktif = QLabel(BarangForm)
        self.labelUserAktif.setObjectName(u"labelUserAktif")

        self.verticalLayout.addWidget(self.labelUserAktif)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.labelKode = QLabel(BarangForm)
        self.labelKode.setObjectName(u"labelKode")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelKode)

        self.input_kode = QLineEdit(BarangForm)
        self.input_kode.setObjectName(u"input_kode")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.input_kode)

        self.labelNama = QLabel(BarangForm)
        self.labelNama.setObjectName(u"labelNama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelNama)

        self.input_nama = QLineEdit(BarangForm)
        self.input_nama.setObjectName(u"input_nama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.input_nama)

        self.labelHarga = QLabel(BarangForm)
        self.labelHarga.setObjectName(u"labelHarga")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelHarga)

        self.input_harga = QLineEdit(BarangForm)
        self.input_harga.setObjectName(u"input_harga")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.input_harga)

        self.labelStok = QLabel(BarangForm)
        self.labelStok.setObjectName(u"labelStok")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.labelStok)

        self.input_stok = QLineEdit(BarangForm)
        self.input_stok.setObjectName(u"input_stok")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.input_stok)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnSimpan = QPushButton(BarangForm)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.buttonLayout.addWidget(self.btnSimpan)

        self.btnUbah = QPushButton(BarangForm)
        self.btnUbah.setObjectName(u"btnUbah")

        self.buttonLayout.addWidget(self.btnUbah)

        self.btnHapus = QPushButton(BarangForm)
        self.btnHapus.setObjectName(u"btnHapus")

        self.buttonLayout.addWidget(self.btnHapus)

        self.btnBersih = QPushButton(BarangForm)
        self.btnBersih.setObjectName(u"btnBersih")

        self.buttonLayout.addWidget(self.btnBersih)

        self.btnPrint = QPushButton(BarangForm)
        self.btnPrint.setObjectName(u"btnPrint")

        self.buttonLayout.addWidget(self.btnPrint)


        self.verticalLayout.addLayout(self.buttonLayout)

        self.input_cari = QLineEdit(BarangForm)
        self.input_cari.setObjectName(u"input_cari")

        self.verticalLayout.addWidget(self.input_cari)

        self.tableBarang = QTableWidget(BarangForm)
        if (self.tableBarang.columnCount() < 5):
            self.tableBarang.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableBarang.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableBarang.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableBarang.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableBarang.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableBarang.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableBarang.setObjectName(u"tableBarang")
        self.tableBarang.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.verticalLayout.addWidget(self.tableBarang)


        self.retranslateUi(BarangForm)

        QMetaObject.connectSlotsByName(BarangForm)
    # setupUi

    def retranslateUi(self, BarangForm):
        BarangForm.setWindowTitle(QCoreApplication.translate("BarangForm", u"Form Data Barang", None))
        self.labelTitle.setText(QCoreApplication.translate("BarangForm", u"Manajemen Data Barang", None))
        self.labelUserAktif.setText(QCoreApplication.translate("BarangForm", u"User Aktif: -", None))
        self.labelKode.setText(QCoreApplication.translate("BarangForm", u"Kode", None))
        self.labelNama.setText(QCoreApplication.translate("BarangForm", u"Nama", None))
        self.labelHarga.setText(QCoreApplication.translate("BarangForm", u"Harga", None))
        self.labelStok.setText(QCoreApplication.translate("BarangForm", u"Stok", None))
        self.btnSimpan.setText(QCoreApplication.translate("BarangForm", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("BarangForm", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("BarangForm", u"Hapus", None))
        self.btnBersih.setText(QCoreApplication.translate("BarangForm", u"Bersih", None))
        self.btnPrint.setText(QCoreApplication.translate("BarangForm", u"Print", None))
        self.input_cari.setPlaceholderText(QCoreApplication.translate("BarangForm", u"Cari berdasarkan kode atau nama..", None))
        ___qtablewidgetitem = self.tableBarang.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("BarangForm", u"ID", None));
        ___qtablewidgetitem1 = self.tableBarang.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("BarangForm", u"Kode", None));
        ___qtablewidgetitem2 = self.tableBarang.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("BarangForm", u"Nama", None));
        ___qtablewidgetitem3 = self.tableBarang.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("BarangForm", u"Harga", None));
        ___qtablewidgetitem4 = self.tableBarang.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("BarangForm", u"Stok", None));
    # retranslateUi

