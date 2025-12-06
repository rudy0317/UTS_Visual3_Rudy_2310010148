# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'barang_keluar_form.ui'
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

class Ui_BarangKeluarForm(object):
    def setupUi(self, BarangKeluarForm):
        if not BarangKeluarForm.objectName():
            BarangKeluarForm.setObjectName(u"BarangKeluarForm")
        BarangKeluarForm.resize(800, 600)
        self.verticalLayout = QVBoxLayout(BarangKeluarForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelTitle = QLabel(BarangKeluarForm)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setStyleSheet(u"font-size:20px; font-weight:bold;")
        self.labelTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.labelTitle)

        self.labelUserAktif = QLabel(BarangKeluarForm)
        self.labelUserAktif.setObjectName(u"labelUserAktif")
        self.labelUserAktif.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.labelUserAktif)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.labelBarang = QLabel(BarangKeluarForm)
        self.labelBarang.setObjectName(u"labelBarang")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelBarang)

        self.comboBarang = QComboBox(BarangKeluarForm)
        self.comboBarang.setObjectName(u"comboBarang")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.comboBarang)

        self.labelTanggal = QLabel(BarangKeluarForm)
        self.labelTanggal.setObjectName(u"labelTanggal")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelTanggal)

        self.input_tanggal = QDateEdit(BarangKeluarForm)
        self.input_tanggal.setObjectName(u"input_tanggal")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.input_tanggal)

        self.labelJumlah = QLabel(BarangKeluarForm)
        self.labelJumlah.setObjectName(u"labelJumlah")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelJumlah)

        self.input_jumlah = QSpinBox(BarangKeluarForm)
        self.input_jumlah.setObjectName(u"input_jumlah")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.input_jumlah)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnSimpan = QPushButton(BarangKeluarForm)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.buttonLayout.addWidget(self.btnSimpan)

        self.btnUbah = QPushButton(BarangKeluarForm)
        self.btnUbah.setObjectName(u"btnUbah")

        self.buttonLayout.addWidget(self.btnUbah)

        self.btnHapus = QPushButton(BarangKeluarForm)
        self.btnHapus.setObjectName(u"btnHapus")

        self.buttonLayout.addWidget(self.btnHapus)

        self.btnBersih = QPushButton(BarangKeluarForm)
        self.btnBersih.setObjectName(u"btnBersih")

        self.buttonLayout.addWidget(self.btnBersih)

        self.btnPrint = QPushButton(BarangKeluarForm)
        self.btnPrint.setObjectName(u"btnPrint")

        self.buttonLayout.addWidget(self.btnPrint)


        self.verticalLayout.addLayout(self.buttonLayout)

        self.input_cari = QLineEdit(BarangKeluarForm)
        self.input_cari.setObjectName(u"input_cari")

        self.verticalLayout.addWidget(self.input_cari)

        self.tableBarangKeluar = QTableWidget(BarangKeluarForm)
        if (self.tableBarangKeluar.columnCount() < 6):
            self.tableBarangKeluar.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableBarangKeluar.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableBarangKeluar.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableBarangKeluar.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableBarangKeluar.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableBarangKeluar.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableBarangKeluar.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableBarangKeluar.setObjectName(u"tableBarangKeluar")
        self.tableBarangKeluar.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.verticalLayout.addWidget(self.tableBarangKeluar)


        self.retranslateUi(BarangKeluarForm)

        QMetaObject.connectSlotsByName(BarangKeluarForm)
    # setupUi

    def retranslateUi(self, BarangKeluarForm):
        BarangKeluarForm.setWindowTitle(QCoreApplication.translate("BarangKeluarForm", u"Form Barang Keluar", None))
        self.labelTitle.setText(QCoreApplication.translate("BarangKeluarForm", u"Transaksi Barang Keluar", None))
        self.labelUserAktif.setText(QCoreApplication.translate("BarangKeluarForm", u"User Aktif: -", None))
        self.labelBarang.setText(QCoreApplication.translate("BarangKeluarForm", u"Barang", None))
        self.labelTanggal.setText(QCoreApplication.translate("BarangKeluarForm", u"Tanggal", None))
        self.labelJumlah.setText(QCoreApplication.translate("BarangKeluarForm", u"Jumlah", None))
        self.btnSimpan.setText(QCoreApplication.translate("BarangKeluarForm", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("BarangKeluarForm", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("BarangKeluarForm", u"Hapus", None))
        self.btnBersih.setText(QCoreApplication.translate("BarangKeluarForm", u"Bersih", None))
        self.btnPrint.setText(QCoreApplication.translate("BarangKeluarForm", u"Print", None))
        self.input_cari.setPlaceholderText(QCoreApplication.translate("BarangKeluarForm", u"Cari berdasarkan kode atau nama..", None))
        ___qtablewidgetitem = self.tableBarangKeluar.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("BarangKeluarForm", u"ID Keluar", None));
        ___qtablewidgetitem1 = self.tableBarangKeluar.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("BarangKeluarForm", u"Kode Barang", None));
        ___qtablewidgetitem2 = self.tableBarangKeluar.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("BarangKeluarForm", u"Nama Barang", None));
        ___qtablewidgetitem3 = self.tableBarangKeluar.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("BarangKeluarForm", u"Tanggal", None));
        ___qtablewidgetitem4 = self.tableBarangKeluar.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("BarangKeluarForm", u"Jumlah", None));
        ___qtablewidgetitem5 = self.tableBarangKeluar.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("BarangKeluarForm", u"User", None));
    # retranslateUi

