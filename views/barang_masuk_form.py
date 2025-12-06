# views/barang_masuk_form.py
import os
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QVBoxLayout, QAbstractItemView
from PySide6.QtCore import QFile, QDate
from PySide6.QtUiTools import QUiLoader
from models.barang_masuk_model import BarangMasukModel
from models.barang_model import BarangModel


class BarangMasukForm(QWidget):
    def __init__(self, current_user, parent=None):
        super().__init__(parent)

        # Path UI absolut
        ui_path = os.path.join(os.path.dirname(__file__), "..", "ui", "barang_masuk_form.ui")
        abs_path = os.path.abspath(ui_path)

        if not os.path.exists(abs_path):
            QMessageBox.critical(self, "Error", f"File UI tidak ditemukan:\n{abs_path}")
            return

        loader = QUiLoader()
        ui_file = QFile(abs_path)
        ui_file.open(QFile.ReadOnly)
        form = loader.load(ui_file, self)
        ui_file.close()

        # tempel ke layout biar tampil
        layout = QVBoxLayout(self)
        layout.addWidget(form)
        layout.setContentsMargins(0, 0, 0, 0)

        # pakai nama ala dosen
        self.formBarangMasuk = form
        self.aksiCrud = BarangMasukModel()
        self.barangModel = BarangModel()
        self.current_user = current_user

        self.setWindowTitle("Manajemen Data Barang Masuk")

        # Set label user aktif
        if self.current_user:
            self.formBarangMasuk.labelUserAktif.setText(f"User Aktif: {self.current_user['nama']}")
        else:
            self.formBarangMasuk.labelUserAktif.setText("User Aktif: -")

        # Set default tanggal ke hari ini
        self.formBarangMasuk.input_tanggal.setDate(QDate.currentDate())

        # Load combo barang
        self.loadComboBarang()

        # Hubungkan tombol
        self.formBarangMasuk.btnSimpan.clicked.connect(self.SimpanBarangMasuk)
        self.formBarangMasuk.btnUbah.clicked.connect(self.UbahBarangMasuk)
        self.formBarangMasuk.btnHapus.clicked.connect(self.HapusBarangMasuk)
        self.formBarangMasuk.btnBersih.clicked.connect(self.BersihForm)

        self.formBarangMasuk.tableBarangMasuk.itemSelectionChanged.connect(self.isiFormDariTabel)
        self.formBarangMasuk.tableBarangMasuk.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.formBarangMasuk.input_cari.textChanged.connect(self.filterDataBarangMasuk)
        self.formBarangMasuk.btnPrint.clicked.connect(self.CetakLaporanMasuk)

        # pertama kali tampil
        self.tampilDataBarangMasuk()

    def loadComboBarang(self):
        data = self.barangModel.dataBarang()
        self.formBarangMasuk.comboBarang.clear()
        for baris in data:
            display_text = f"{baris['kode']} - {baris['nama']}"
            self.formBarangMasuk.comboBarang.addItem(display_text, baris["id_barang"])

    # ===================== TAMPIL DATA =====================
    def tampilDataBarangMasuk(self):
        self.formBarangMasuk.tableBarangMasuk.setRowCount(0)
        data = self.aksiCrud.dataBarangMasuk()

        for i, baris in enumerate(data):
            self.formBarangMasuk.tableBarangMasuk.insertRow(i)
            self.formBarangMasuk.tableBarangMasuk.setItem(i, 0, QTableWidgetItem(str(baris["id_masuk"])))
            self.formBarangMasuk.tableBarangMasuk.setItem(i, 1, QTableWidgetItem(baris["kode"]))
            self.formBarangMasuk.tableBarangMasuk.setItem(i, 2, QTableWidgetItem(baris["nama"]))
            self.formBarangMasuk.tableBarangMasuk.setItem(i, 3, QTableWidgetItem(str(baris["tanggal"])))
            self.formBarangMasuk.tableBarangMasuk.setItem(i, 4, QTableWidgetItem(str(baris["jumlah"])))
            self.formBarangMasuk.tableBarangMasuk.setItem(i, 5, QTableWidgetItem(baris["nama_user"] or ""))

    def CetakLaporanMasuk(self):
        self.aksiCrud.laporanBarangMasuk()

    # ===================== BERSIHKAN FORM =====================
    def BersihForm(self):
        self.formBarangMasuk.comboBarang.setCurrentIndex(-1)
        self.formBarangMasuk.input_tanggal.setDate(QDate.currentDate())
        self.formBarangMasuk.input_jumlah.setValue(0)
        self.formBarangMasuk.tableBarangMasuk.clearSelection()

    # ===================== AMBIL DATA DARI FORM =====================
    def ambilDataForm(self):
        id_barang = self.formBarangMasuk.comboBarang.currentData()
        tanggal = self.formBarangMasuk.input_tanggal.date().toString("yyyy-MM-dd")
        jumlah = self.formBarangMasuk.input_jumlah.value()
        id_user = self.current_user["id_user"] if self.current_user else None
        return id_barang, tanggal, jumlah, id_user

    # ===================== VALIDASI DATA BARANG MASUK =====================
    def ValidasiBarangMasuk(self, mode="tambah", id_masuk=None):
        id_barang, tanggal, jumlah, id_user = self.ambilDataForm()

        if id_barang is None or id_barang == 0:
            QMessageBox.warning(self, "Peringatan", "Barang wajib dipilih!")
            return False

        if jumlah <= 0:
            QMessageBox.warning(self, "Peringatan", "Jumlah harus lebih dari 0!")
            return False

        if tanggal == "":
            QMessageBox.warning(self, "Peringatan", "Tanggal wajib diisi!")
            return False

        return True

    # ===================== SIMPAN =====================
    def SimpanBarangMasuk(self):
        if not self.ValidasiBarangMasuk(mode="tambah"):
            return

        id_barang, tanggal, jumlah, id_user = self.ambilDataForm()
        self.aksiCrud.simpanDataBarangMasuk(id_barang, tanggal, jumlah, id_user)
        self.tampilDataBarangMasuk()
        self.BersihForm()
        QMessageBox.information(self, "Info", "Data berhasil disimpan")

    # ===================== UBAH =====================
    def UbahBarangMasuk(self):
        baris = self.formBarangMasuk.tableBarangMasuk.currentRow()
        if baris < 0:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang mau diubah!")
            return

        id_masuk = int(self.formBarangMasuk.tableBarangMasuk.item(baris, 0).text())

        if not self.ValidasiBarangMasuk(mode="ubah", id_masuk=id_masuk):
            return

        id_barang, tanggal, jumlah, id_user = self.ambilDataForm()
        self.aksiCrud.ubahDataBarangMasuk(id_barang, tanggal, jumlah, id_user, id_masuk)
        self.tampilDataBarangMasuk()
        self.BersihForm()
        QMessageBox.information(self, "Info", "Data berhasil diubah")

    # ===================== HAPUS =====================
    def HapusBarangMasuk(self):
        baris = self.formBarangMasuk.tableBarangMasuk.currentRow()
        if baris < 0:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang mau dihapus!")
            return

        id_masuk = int(self.formBarangMasuk.tableBarangMasuk.item(baris, 0).text())

        tanya = QMessageBox.question(
            self,
            "Konfirmasi",
            "Apakah Anda yakin ingin menghapus data ini?",
            QMessageBox.Yes | QMessageBox.No
        )

        if tanya == QMessageBox.Yes:
            self.aksiCrud.hapusDataBarangMasuk(id_masuk)
            self.tampilDataBarangMasuk()
            self.BersihForm()
            QMessageBox.information(self, "Info", "Data berhasil dihapus")

    # ===================== ISI FORM DARI TABEL =====================
    def isiFormDariTabel(self):
        baris = self.formBarangMasuk.tableBarangMasuk.currentRow()
        if baris < 0:
            return

        kode = self.formBarangMasuk.tableBarangMasuk.item(baris, 1).text()
        nama = self.formBarangMasuk.tableBarangMasuk.item(baris, 2).text()
        display_text = f"{kode} - {nama}"
        index = self.formBarangMasuk.comboBarang.findText(display_text)
        if index >= 0:
            self.formBarangMasuk.comboBarang.setCurrentIndex(index)

        tanggal_str = self.formBarangMasuk.tableBarangMasuk.item(baris, 3).text()
        tanggal = QDate.fromString(tanggal_str, "yyyy-MM-dd")
        self.formBarangMasuk.input_tanggal.setDate(tanggal)

        jumlah = int(self.formBarangMasuk.tableBarangMasuk.item(baris, 4).text())
        self.formBarangMasuk.input_jumlah.setValue(jumlah)

    # ===================== FILTER DATA =====================
    def filterDataBarangMasuk(self):
        kata = self.formBarangMasuk.input_cari.text()
        self.formBarangMasuk.tableBarangMasuk.setRowCount(0)

        if kata == "":
            data = self.aksiCrud.dataBarangMasuk()
        else:
            data = self.aksiCrud.filterBarangMasuk(kata)

        for i, baris in enumerate(data):
            self.formBarangMasuk.tableBarangMasuk.insertRow(i)
            self.formBarangMasuk.tableBarangMasuk.setItem(i, 0, QTableWidgetItem(str(baris["id_masuk"])))
            self.formBarangMasuk.tableBarangMasuk.setItem(i, 1, QTableWidgetItem(baris["kode"]))
            self.formBarangMasuk.tableBarangMasuk.setItem(i, 2, QTableWidgetItem(baris["nama"]))
            self.formBarangMasuk.tableBarangMasuk.setItem(i, 3, QTableWidgetItem(str(baris["tanggal"])))
            self.formBarangMasuk.tableBarangMasuk.setItem(i, 4, QTableWidgetItem(str(baris["jumlah"])))
            self.formBarangMasuk.tableBarangMasuk.setItem(i, 5, QTableWidgetItem(baris["nama_user"] or ""))
