# views/barang_form.py
import os
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QVBoxLayout, QAbstractItemView
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from models.barang_model import BarangModel



class BarangForm(QWidget):
    def __init__(self, current_user, parent=None):
        super().__init__(parent)

        # Path UI absolut
        ui_path = os.path.join(os.path.dirname(__file__), "..", "ui", "barang_form.ui")
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
        self.formBarang = form
        self.aksiCrud = BarangModel()
        self.current_user = current_user

        self.setWindowTitle("Manajemen Data Barang")

        # Set label user aktif
        if self.current_user:
            self.formBarang.labelUserAktif.setText(f"User Aktif: {self.current_user['nama']}")
        else:
            self.formBarang.labelUserAktif.setText("User Aktif: -")

        # Hubungkan tombol
        self.formBarang.btnSimpan.clicked.connect(self.SimpanBarang)
        self.formBarang.btnUbah.clicked.connect(self.UbahBarang)
        self.formBarang.btnHapus.clicked.connect(self.HapusBarang)
        self.formBarang.btnBersih.clicked.connect(self.BersihForm)
        self.formBarang.btnPrint.clicked.connect(self.CetakLaporan)
        self.formBarang.tableBarang.itemSelectionChanged.connect(self.isiFormDariTabel)
        self.formBarang.tableBarang.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.formBarang.input_cari.textChanged.connect(self.filterDataBarang)

        # pertama kali tampil
        self.tampilDataBarang()


    # ===================== TAMPIL DATA =====================
    def tampilDataBarang(self):
        self.formBarang.tableBarang.setRowCount(0)
        data = self.aksiCrud.dataBarang()

        for i, baris in enumerate(data):
            self.formBarang.tableBarang.insertRow(i)
            self.formBarang.tableBarang.setItem(i, 0, QTableWidgetItem(str(baris["id_barang"])))
            self.formBarang.tableBarang.setItem(i, 1, QTableWidgetItem(baris["kode"]))
            self.formBarang.tableBarang.setItem(i, 2, QTableWidgetItem(baris["nama"]))
            self.formBarang.tableBarang.setItem(i, 3, QTableWidgetItem(str(baris["harga"])))
            self.formBarang.tableBarang.setItem(i, 4, QTableWidgetItem(str(baris["stok"])))

    # ===================== BERSIHKAN FORM =====================
    def BersihForm(self):
        self.formBarang.input_kode.clear()
        self.formBarang.input_nama.clear()
        self.formBarang.input_harga.clear()
        self.formBarang.input_stok.clear()
        self.formBarang.tableBarang.clearSelection()

    # ===================== AMBIL DATA DARI FORM =====================
    def ambilDataForm(self):
        kode = self.formBarang.input_kode.text().strip()
        nama = self.formBarang.input_nama.text().strip()
        harga = int(self.formBarang.input_harga.text() or 0)
        stok = int(self.formBarang.input_stok.text() or 0)
        return kode, nama, harga, stok

    # ===================== VALIDASI DATA BARANG =====================
    def ValidasiBarang(self, mode="tambah", id_barang=None):
        kode, nama, harga, stok = self.ambilDataForm()

        if kode == "" or nama == "":
            QMessageBox.warning(self, "Peringatan", "Kode dan Nama wajib diisi!")
            return False

        if harga <= 0:
            QMessageBox.warning(self, "Peringatan", "Harga harus lebih dari 0!")
            return False

        if stok < 0:
            QMessageBox.warning(self, "Peringatan", "Stok tidak boleh negatif!")
            return False

        # cek duplikat kode
        if mode == "tambah":
            if self.aksiCrud.cekKodeBarang(kode) > 0:
                QMessageBox.warning(self, "Peringatan", "Kode barang sudah digunakan, silakan pakai kode lain!")
                return False

        if mode == "ubah" and id_barang is not None:
            if self.aksiCrud.cekKodeBarangLain(kode, id_barang) > 0:
                QMessageBox.warning(self, "Peringatan", "Kode barang sudah dipakai data lain!")
                return False

        return True

    # ===================== SIMPAN =====================
    def SimpanBarang(self):
        if not self.ValidasiBarang(mode="tambah"):
            return

        kode, nama, harga, stok = self.ambilDataForm()
        self.aksiCrud.simpanDataBarang(kode, nama, harga, stok)
        self.tampilDataBarang()
        self.BersihForm()
        QMessageBox.information(self, "Info", "Data berhasil disimpan")

    # ===================== UBAH =====================
    def UbahBarang(self):
        baris = self.formBarang.tableBarang.currentRow()
        if baris < 0:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang mau diubah!")
            return

        id_barang = int(self.formBarang.tableBarang.item(baris, 0).text())

        if not self.ValidasiBarang(mode="ubah", id_barang=id_barang):
            return

        kode, nama, harga, stok = self.ambilDataForm()
        self.aksiCrud.ubahDataBarang(kode, nama, harga, stok, id_barang)
        self.tampilDataBarang()
        self.BersihForm()
        QMessageBox.information(self, "Info", "Data berhasil diubah")

    # ===================== HAPUS =====================
    def HapusBarang(self):
        baris = self.formBarang.tableBarang.currentRow()
        if baris < 0:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang mau dihapus!")
            return

        id_barang = int(self.formBarang.tableBarang.item(baris, 0).text())

        # CEK DULU: BARANG SUDAH DIPAKAI DI TABEL MASUK/KELUAR BELUM?
        if self.aksiCrud.cekBarangDipakai(id_barang) > 0:
            QMessageBox.warning(
                self,
                "Peringatan",
                "Data barang ini tidak bisa dihapus karena sudah dipakai\n"
                "di tabel barang masuk / barang keluar."
            )
            return

        tanya = QMessageBox.question(
            self,
            "Konfirmasi",
            "Apakah Anda yakin ingin menghapus data ini?",
            QMessageBox.Yes | QMessageBox.No
        )

        if tanya == QMessageBox.Yes:
            self.aksiCrud.hapusDataBarang(id_barang)
            self.tampilDataBarang()
            self.BersihForm()
            QMessageBox.information(self, "Info", "Data berhasil dihapus")


    # ===================== ISI FORM DARI TABEL =====================
    def isiFormDariTabel(self):
        baris = self.formBarang.tableBarang.currentRow()
        if baris < 0:
            return

        self.formBarang.input_kode.setText(self.formBarang.tableBarang.item(baris, 1).text())
        self.formBarang.input_nama.setText(self.formBarang.tableBarang.item(baris, 2).text())
        self.formBarang.input_harga.setText(self.formBarang.tableBarang.item(baris, 3).text())
        self.formBarang.input_stok.setText(self.formBarang.tableBarang.item(baris, 4).text())

    # ===================== FILTER DATA =====================
    def filterDataBarang(self):
        kata = self.formBarang.input_cari.text()
        self.formBarang.tableBarang.setRowCount(0)

        if kata == "":
            data = self.aksiCrud.dataBarang()
        else:
            data = self.aksiCrud.filterBarang(kata)

        for i, baris in enumerate(data):
            self.formBarang.tableBarang.insertRow(i)
            self.formBarang.tableBarang.setItem(i, 0, QTableWidgetItem(str(baris["id_barang"])))
            self.formBarang.tableBarang.setItem(i, 1, QTableWidgetItem(baris["kode"]))
            self.formBarang.tableBarang.setItem(i, 2, QTableWidgetItem(baris["nama"]))
            self.formBarang.tableBarang.setItem(i, 3, QTableWidgetItem(str(baris["harga"])))
            self.formBarang.tableBarang.setItem(i, 4, QTableWidgetItem(str(baris["stok"])))

    def CetakLaporan(self):
        self.aksiCrud.laporanBarang()
