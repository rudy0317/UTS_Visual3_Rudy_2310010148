# views/instansi_form.py
import os
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QVBoxLayout, QAbstractItemView
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from models.instansi_model import InstansiModel
from models.user_model import UserModel


class InstansiForm(QWidget):
    def __init__(self, current_user, parent=None):
        super().__init__(parent)

        # Path UI absolut
        ui_path = os.path.join(os.path.dirname(__file__), "..", "ui", "instansi_form.ui")
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
        self.formInstansi = form
        self.aksiCrud = InstansiModel()
        self.userModel = UserModel()
        self.current_user = current_user

        self.setWindowTitle("Manajemen Data Instansi")

        # Set label user aktif
        if self.current_user:
            self.formInstansi.labelUserAktif.setText(f"User Aktif: {self.current_user['nama']}")
        else:
            self.formInstansi.labelUserAktif.setText("User Aktif: -")

        # Load combo admin
        self.loadComboAdmin()

        # Hubungkan tombol
        self.formInstansi.btnSimpan.clicked.connect(self.SimpanInstansi)
        self.formInstansi.btnUbah.clicked.connect(self.UbahInstansi)
        self.formInstansi.btnHapus.clicked.connect(self.HapusInstansi)
        self.formInstansi.btnBersih.clicked.connect(self.BersihForm)

        self.formInstansi.tableInstansi.itemSelectionChanged.connect(self.isiFormDariTabel)
        self.formInstansi.tableInstansi.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.formInstansi.input_cari.textChanged.connect(self.filterDataInstansi)
        self.formInstansi.btnPrint.clicked.connect(self.CetakLaporanInstansi)

        # pertama kali tampil
        self.tampilDataInstansi()

    def loadComboAdmin(self):
        data = self.userModel.get_all()
        self.formInstansi.combo_admin.clear()
        for baris in data:
            self.formInstansi.combo_admin.addItem(baris["nama"], baris["id_user"])

    # ===================== TAMPIL DATA =====================
    def tampilDataInstansi(self):
        self.formInstansi.tableInstansi.setRowCount(0)
        data = self.aksiCrud.dataInstansi()

        for i, baris in enumerate(data):
            self.formInstansi.tableInstansi.insertRow(i)
            self.formInstansi.tableInstansi.setItem(i, 0, QTableWidgetItem(str(baris["id_instansi"])))
            self.formInstansi.tableInstansi.setItem(i, 1, QTableWidgetItem(baris["nama_instansi"]))
            self.formInstansi.tableInstansi.setItem(i, 2, QTableWidgetItem(baris["alamat"]))
            self.formInstansi.tableInstansi.setItem(i, 3, QTableWidgetItem(baris["kontak"] or ""))
            self.formInstansi.tableInstansi.setItem(i, 4, QTableWidgetItem(baris["nama_admin"] or ""))

    def CetakLaporanInstansi(self):
        self.aksiCrud.laporanInstansi()

    # ===================== BERSIHKAN FORM =====================
    def BersihForm(self):
        self.formInstansi.input_nama_instansi.clear()
        self.formInstansi.input_alamat.clear()
        self.formInstansi.input_kontak.clear()
        self.formInstansi.combo_admin.setCurrentIndex(-1)
        self.formInstansi.tableInstansi.clearSelection()

    # ===================== AMBIL DATA DARI FORM =====================
    def ambilDataForm(self):
        nama_instansi = self.formInstansi.input_nama_instansi.text().strip()
        alamat = self.formInstansi.input_alamat.toPlainText().strip()
        kontak = self.formInstansi.input_kontak.text().strip()
        id_admin = self.formInstansi.combo_admin.currentData()
        return nama_instansi, alamat, kontak, id_admin

    # ===================== VALIDASI DATA INSTANSI =====================
    def ValidasiInstansi(self, mode="tambah", id_instansi=None):
        nama_instansi, alamat, kontak, id_admin = self.ambilDataForm()

        if nama_instansi == "":
            QMessageBox.warning(self, "Peringatan", "Nama Instansi wajib diisi!")
            return False

        if alamat == "":
            QMessageBox.warning(self, "Peringatan", "Alamat wajib diisi!")
            return False

        return True

    # ===================== SIMPAN =====================
    def SimpanInstansi(self):
        if not self.ValidasiInstansi(mode="tambah"):
            return

        nama_instansi, alamat, kontak, id_admin = self.ambilDataForm()
        self.aksiCrud.simpanDataInstansi(nama_instansi, alamat, kontak, id_admin)
        self.tampilDataInstansi()
        self.BersihForm()
        QMessageBox.information(self, "Info", "Data berhasil disimpan")

    # ===================== UBAH =====================
    def UbahInstansi(self):
        baris = self.formInstansi.tableInstansi.currentRow()
        if baris < 0:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang mau diubah!")
            return

        id_instansi = int(self.formInstansi.tableInstansi.item(baris, 0).text())

        if not self.ValidasiInstansi(mode="ubah", id_instansi=id_instansi):
            return

        nama_instansi, alamat, kontak, id_admin = self.ambilDataForm()
        self.aksiCrud.ubahDataInstansi(nama_instansi, alamat, kontak, id_admin, id_instansi)
        self.tampilDataInstansi()
        self.BersihForm()
        QMessageBox.information(self, "Info", "Data berhasil diubah")

    # ===================== HAPUS =====================
    def HapusInstansi(self):
        baris = self.formInstansi.tableInstansi.currentRow()
        if baris < 0:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang mau dihapus!")
            return

        id_instansi = int(self.formInstansi.tableInstansi.item(baris, 0).text())

        tanya = QMessageBox.question(
            self,
            "Konfirmasi",
            "Apakah Anda yakin ingin menghapus data ini?",
            QMessageBox.Yes | QMessageBox.No
        )

        if tanya == QMessageBox.Yes:
            self.aksiCrud.hapusDataInstansi(id_instansi)
            self.tampilDataInstansi()
            self.BersihForm()
            QMessageBox.information(self, "Info", "Data berhasil dihapus")

    # ===================== ISI FORM DARI TABEL =====================
    def isiFormDariTabel(self):
        baris = self.formInstansi.tableInstansi.currentRow()
        if baris < 0:
            return

        self.formInstansi.input_nama_instansi.setText(self.formInstansi.tableInstansi.item(baris, 1).text())
        self.formInstansi.input_alamat.setPlainText(self.formInstansi.tableInstansi.item(baris, 2).text())
        self.formInstansi.input_kontak.setText(self.formInstansi.tableInstansi.item(baris, 3).text())

        nama_admin = self.formInstansi.tableInstansi.item(baris, 4).text()
        index = self.formInstansi.combo_admin.findText(nama_admin)
        if index >= 0:
            self.formInstansi.combo_admin.setCurrentIndex(index)

    # ===================== FILTER DATA =====================
    def filterDataInstansi(self):
        kata = self.formInstansi.input_cari.text()
        self.formInstansi.tableInstansi.setRowCount(0)

        if kata == "":
            data = self.aksiCrud.dataInstansi()
        else:
            data = self.aksiCrud.filterInstansi(kata)

        for i, baris in enumerate(data):
            self.formInstansi.tableInstansi.insertRow(i)
            self.formInstansi.tableInstansi.setItem(i, 0, QTableWidgetItem(str(baris["id_instansi"])))
            self.formInstansi.tableInstansi.setItem(i, 1, QTableWidgetItem(baris["nama_instansi"]))
            self.formInstansi.tableInstansi.setItem(i, 2, QTableWidgetItem(baris["alamat"]))
            self.formInstansi.tableInstansi.setItem(i, 3, QTableWidgetItem(baris["kontak"] or ""))
            self.formInstansi.tableInstansi.setItem(i, 4, QTableWidgetItem(baris["nama_admin"] or ""))
