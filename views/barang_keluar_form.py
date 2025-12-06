# views/barang_keluar_form.py
import os
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QVBoxLayout, QAbstractItemView
from PySide6.QtCore import QFile, QDate
from PySide6.QtUiTools import QUiLoader
from models.barang_keluar_model import BarangKeluarModel
from models.barang_model import BarangModel


class BarangKeluarForm(QWidget):
    def __init__(self, current_user, parent=None):
        super().__init__(parent)

        ui_path = os.path.join(os.path.dirname(__file__), "..", "ui", "barang_keluar_form.ui")
        abs_path = os.path.abspath(ui_path)

        if not os.path.exists(abs_path):
            QMessageBox.critical(self, "Error", f"File UI tidak ditemukan:\n{abs_path}")
            return

        loader = QUiLoader()
        ui_file = QFile(abs_path)
        ui_file.open(QFile.ReadOnly)
        form = loader.load(ui_file, self)
        ui_file.close()

        layout = QVBoxLayout(self)
        layout.addWidget(form)
        layout.setContentsMargins(0, 0, 0, 0)

        self.formBarangKeluar = form
        self.aksiCrud = BarangKeluarModel()
        self.barangModel = BarangModel()
        self.current_user = current_user

        self.setWindowTitle("Manajemen Data Barang Keluar")

        if self.current_user:
            self.formBarangKeluar.labelUserAktif.setText(f"User Aktif: {self.current_user['nama']}")
        else:
            self.formBarangKeluar.labelUserAktif.setText("User Aktif: -")

        self.formBarangKeluar.input_tanggal.setDate(QDate.currentDate())

        self.loadComboBarang()

        self.formBarangKeluar.btnSimpan.clicked.connect(self.SimpanBarangKeluar)
        self.formBarangKeluar.btnUbah.clicked.connect(self.UbahBarangKeluar)
        self.formBarangKeluar.btnHapus.clicked.connect(self.HapusBarangKeluar)
        self.formBarangKeluar.btnBersih.clicked.connect(self.BersihForm)

        self.formBarangKeluar.tableBarangKeluar.itemSelectionChanged.connect(self.isiFormDariTabel)
        self.formBarangKeluar.tableBarangKeluar.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.formBarangKeluar.input_cari.textChanged.connect(self.filterDataBarangKeluar)
        self.formBarangKeluar.btnPrint.clicked.connect(self.CekLaporanKeluar)

        self.tampilDataBarangKeluar()

    def loadComboBarang(self):
        data = self.barangModel.dataBarang()
        self.formBarangKeluar.comboBarang.clear()
        for baris in data:
            display_text = f"{baris['kode']} - {baris['nama']}"
            self.formBarangKeluar.comboBarang.addItem(display_text, baris["id_barang"])

    # ===================== TAMPIL DATA =====================
    def tampilDataBarangKeluar(self):
        self.formBarangKeluar.tableBarangKeluar.setRowCount(0)
        data = self.aksiCrud.dataBarangKeluar()

        for i, baris in enumerate(data):
            self.formBarangKeluar.tableBarangKeluar.insertRow(i)
            self.formBarangKeluar.tableBarangKeluar.setItem(i, 0, QTableWidgetItem(str(baris["id_keluar"])))
            self.formBarangKeluar.tableBarangKeluar.setItem(i, 1, QTableWidgetItem(baris["kode"]))
            self.formBarangKeluar.tableBarangKeluar.setItem(i, 2, QTableWidgetItem(baris["nama"]))
            self.formBarangKeluar.tableBarangKeluar.setItem(i, 3, QTableWidgetItem(str(baris["tanggal"])))
            self.formBarangKeluar.tableBarangKeluar.setItem(i, 4, QTableWidgetItem(str(baris["jumlah"])))
            self.formBarangKeluar.tableBarangKeluar.setItem(i, 5, QTableWidgetItem(baris["nama_user"] or ""))

    # ===================== BERSIHKAN FORM =====================
    def BersihForm(self):
        self.formBarangKeluar.comboBarang.setCurrentIndex(-1)
        self.formBarangKeluar.input_tanggal.setDate(QDate.currentDate())
        self.formBarangKeluar.input_jumlah.setValue(0)
        self.formBarangKeluar.tableBarangKeluar.clearSelection()

    # ===================== AMBIL DATA DARI FORM =====================
    def ambilDataForm(self):
        id_barang = self.formBarangKeluar.comboBarang.currentData()
        tanggal = self.formBarangKeluar.input_tanggal.date().toString("yyyy-MM-dd")
        jumlah = self.formBarangKeluar.input_jumlah.value()
        id_user = self.current_user["id_user"] if self.current_user else None
        return id_barang, tanggal, jumlah, id_user

    # ===================== VALIDASI DATA BARANG KELUAR =====================
    def ValidasiBarangKeluar(self, mode="tambah", id_keluar=None):
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
    def SimpanBarangKeluar(self):
        if not self.ValidasiBarangKeluar(mode="tambah"):
            return

        id_barang, tanggal, jumlah, id_user = self.ambilDataForm()
        self.aksiCrud.simpanDataBarangKeluar(id_barang, tanggal, jumlah, id_user)
        self.tampilDataBarangKeluar()
        self.BersihForm()
        QMessageBox.information(self, "Info", "Data berhasil disimpan")

    # ===================== UBAH =====================
    def UbahBarangKeluar(self):
        baris = self.formBarangKeluar.tableBarangKeluar.currentRow()
        if baris < 0:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang mau diubah!")
            return

        id_keluar = int(self.formBarangKeluar.tableBarangKeluar.item(baris, 0).text())

        if not self.ValidasiBarangKeluar(mode="ubah", id_keluar=id_keluar):
            return

        id_barang, tanggal, jumlah, id_user = self.ambilDataForm()
        self.aksiCrud.ubahDataBarangKeluar(id_barang, tanggal, jumlah, id_user, id_keluar)
        self.tampilDataBarangKeluar()
        self.BersihForm()
        QMessageBox.information(self, "Info", "Data berhasil diubah")

    # ===================== HAPUS =====================
    def HapusBarangKeluar(self):
        baris = self.formBarangKeluar.tableBarangKeluar.currentRow()
        if baris < 0:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang mau dihapus!")
            return

        id_keluar = int(self.formBarangKeluar.tableBarangKeluar.item(baris, 0).text())

        tanya = QMessageBox.question(
            self,
            "Konfirmasi",
            "Apakah Anda yakin ingin menghapus data ini?",
            QMessageBox.Yes | QMessageBox.No
        )

        if tanya == QMessageBox.Yes:
            self.aksiCrud.hapusDataBarangKeluar(id_keluar)
            self.tampilDataBarangKeluar()
            self.BersihForm()
            QMessageBox.information(self, "Info", "Data berhasil dihapus")

    # ===================== ISI FORM DARI TABEL =====================
    def isiFormDariTabel(self):
        baris = self.formBarangKeluar.tableBarangKeluar.currentRow()
        if baris < 0:
            return

        kode = self.formBarangKeluar.tableBarangKeluar.item(baris, 1).text()
        nama = self.formBarangKeluar.tableBarangKeluar.item(baris, 2).text()
        display_text = f"{kode} - {nama}"
        index = self.formBarangKeluar.comboBarang.findText(display_text)
        if index >= 0:
            self.formBarangKeluar.comboBarang.setCurrentIndex(index)

        tanggal_str = self.formBarangKeluar.tableBarangKeluar.item(baris, 3).text()
        tanggal = QDate.fromString(tanggal_str, "yyyy-MM-dd")
        self.formBarangKeluar.input_tanggal.setDate(tanggal)

        jumlah = int(self.formBarangKeluar.tableBarangKeluar.item(baris, 4).text())
        self.formBarangKeluar.input_jumlah.setValue(jumlah)

    # ===================== FILTER DATA =====================
    def filterDataBarangKeluar(self):
        kata = self.formBarangKeluar.input_cari.text()
        self.formBarangKeluar.tableBarangKeluar.setRowCount(0)

        if kata == "":
            data = self.aksiCrud.dataBarangKeluar()
        else:
            data = self.aksiCrud.filterBarangKeluar(kata)

        for i, baris in enumerate(data):
            self.formBarangKeluar.tableBarangKeluar.insertRow(i)
            self.formBarangKeluar.tableBarangKeluar.setItem(i, 0, QTableWidgetItem(str(baris["id_keluar"])))
            self.formBarangKeluar.tableBarangKeluar.setItem(i, 1, QTableWidgetItem(baris["kode"]))
            self.formBarangKeluar.tableBarangKeluar.setItem(i, 2, QTableWidgetItem(baris["nama"]))
            self.formBarangKeluar.tableBarangKeluar.setItem(i, 3, QTableWidgetItem(str(baris["tanggal"])))
            self.formBarangKeluar.tableBarangKeluar.setItem(i, 4, QTableWidgetItem(str(baris["jumlah"])))
            self.formBarangKeluar.tableBarangKeluar.setItem(i, 5, QTableWidgetItem(baris["nama_user"] or ""))

    def CekLaporanKeluar(self):
        self.aksiCrud.laporanBarangKeluar()
