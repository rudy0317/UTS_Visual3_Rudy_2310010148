# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'barang_masuk_form.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QFormLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_BarangMasukForm(object):
    def setupUi(self, BarangMasukForm):
        if not BarangMasukForm.objectName():
            BarangMasukForm.setObjectName(u"BarangMasukForm")
        BarangMasukForm.resize(800, 600)
        self.verticalLayout = QVBoxLayout(BarangMasukForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelTitle = QLabel(BarangMasukForm)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setStyleSheet(u"font-size:20px; font-weight:bold;")
        self.labelTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.labelTitle)

        self.labelUserAktif = QLabel(BarangMasukForm)
        self.labelUserAktif.setObjectName(u"labelUserAktif")
        self.labelUserAktif.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.labelUserAktif)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.labelBarang = QLabel(BarangMasukForm)
        self.labelBarang.setObjectName(u"labelBarang")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelBarang)

        self.comboBarang = QComboBox(BarangMasukForm)
        self.comboBarang.setObjectName(u"comboBarang")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.comboBarang)

        self.labelTanggal = QLabel(BarangMasukForm)
        self.labelTanggal.setObjectName(u"labelTanggal")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelTanggal)

        self.input_tanggal = QDateEdit(BarangMasukForm)
        self.input_tanggal.setObjectName(u"input_tanggal")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.input_tanggal)

        self.labelJumlah = QLabel(BarangMasukForm)
        self.labelJumlah.setObjectName(u"labelJumlah")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelJumlah)

        self.input_jumlah = QSpinBox(BarangMasukForm)
        self.input_jumlah.setObjectName(u"input_jumlah")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.input_jumlah)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnSimpan = QPushButton(BarangMasukForm)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.buttonLayout.addWidget(self.btnSimpan)

        self.btnUbah = QPushButton(BarangMasukForm)
        self.btnUbah.setObjectName(u"btnUbah")

        self.buttonLayout.addWidget(self.btnUbah)

        self.btnHapus = QPushButton(BarangMasukForm)
        self.btnHapus.setObjectName(u"btnHapus")

        self.buttonLayout.addWidget(self.btnHapus)

        self.btnBersih = QPushButton(BarangMasukForm)
        self.btnBersih.setObjectName(u"btnBersih")

        self.buttonLayout.addWidget(self.btnBersih)

        self.btnPrint = QPushButton(BarangMasukForm)
        self.btnPrint.setObjectName(u"btnPrint")

        self.buttonLayout.addWidget(self.btnPrint)


        self.verticalLayout.addLayout(self.buttonLayout)

        self.input_cari = QLineEdit(BarangMasukForm)
        self.input_cari.setObjectName(u"input_cari")

        self.verticalLayout.addWidget(self.input_cari)

        self.tableBarangMasuk = QTableWidget(BarangMasukForm)
        if (self.tableBarangMasuk.columnCount() < 6):
            self.tableBarangMasuk.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableBarangMasuk.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableBarangMasuk.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableBarangMasuk.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableBarangMasuk.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableBarangMasuk.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableBarangMasuk.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableBarangMasuk.setObjectName(u"tableBarangMasuk")
        self.tableBarangMasuk.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.verticalLayout.addWidget(self.tableBarangMasuk)


        self.retranslateUi(BarangMasukForm)

        QMetaObject.connectSlotsByName(BarangMasukForm)
    # setupUi

    def retranslateUi(self, BarangMasukForm):
        BarangMasukForm.setWindowTitle(QCoreApplication.translate("BarangMasukForm", u"Form Barang Masuk", None))
        self.labelTitle.setText(QCoreApplication.translate("BarangMasukForm", u"Manajemen Barang Masuk", None))
        self.labelUserAktif.setText(QCoreApplication.translate("BarangMasukForm", u"User Aktif: -", None))
        self.labelBarang.setText(QCoreApplication.translate("BarangMasukForm", u"Barang", None))
        self.labelTanggal.setText(QCoreApplication.translate("BarangMasukForm", u"Tanggal", None))
        self.labelJumlah.setText(QCoreApplication.translate("BarangMasukForm", u"Jumlah", None))
        self.btnSimpan.setText(QCoreApplication.translate("BarangMasukForm", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("BarangMasukForm", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("BarangMasukForm", u"Hapus", None))
        self.btnBersih.setText(QCoreApplication.translate("BarangMasukForm", u"Bersih", None))
        self.btnPrint.setText(QCoreApplication.translate("BarangMasukForm", u"Print", None))
        self.input_cari.setPlaceholderText(QCoreApplication.translate("BarangMasukForm", u"Cari berdasarkan kode atau nama..", None))
        ___qtablewidgetitem = self.tableBarangMasuk.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("BarangMasukForm", u"ID Masuk", None));
        ___qtablewidgetitem1 = self.tableBarangMasuk.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("BarangMasukForm", u"Kode Barang", None));
        ___qtablewidgetitem2 = self.tableBarangMasuk.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("BarangMasukForm", u"Nama Barang", None));
        ___qtablewidgetitem3 = self.tableBarangMasuk.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("BarangMasukForm", u"Tanggal", None));
        ___qtablewidgetitem4 = self.tableBarangMasuk.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("BarangMasukForm", u"Jumlah", None));
        ___qtablewidgetitem5 = self.tableBarangMasuk.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("BarangMasukForm", u"User", None));
    # retranslateUi

