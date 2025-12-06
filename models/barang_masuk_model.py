from database.connection import get_connection
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

class BarangMasukModel:
    def __init__(self):
        self.koneksi = get_connection()

    # ===================== TAMPIL DATA =====================
    def dataBarangMasuk(self):
        aksiCur = self.koneksi.cursor(dictionary=True)
        sql = "SELECT bm.*, db.kode, db.nama, u.nama AS nama_user FROM barang_masuk bm JOIN data_barang db ON bm.id_barang = db.id_barang LEFT JOIN users u ON bm.id_user = u.id_user ORDER BY id_masuk ASC"
        aksiCur.execute(sql)
        data = aksiCur.fetchall()
        aksiCur.close()
        return data

    # ===================== FILTER BERDASARKAN NAMA/KODE =====================
    def filterBarangMasuk(self, cari):
        aksiCur = self.koneksi.cursor(dictionary=True)
        sql = "SELECT bm.*, db.kode, db.nama, u.nama AS nama_user FROM barang_masuk bm JOIN data_barang db ON bm.id_barang = db.id_barang LEFT JOIN users u ON bm.id_user = u.id_user WHERE db.nama LIKE %s OR db.kode LIKE %s"
        like = "%" + cari + "%"
        aksiCur.execute(sql, (like, like))
        data = aksiCur.fetchall()
        aksiCur.close()
        return data

    # ===================== CARI BY ID =====================
    def getById(self, id_masuk):
        aksiCur = self.koneksi.cursor(dictionary=True)
        sql = "SELECT * FROM barang_masuk WHERE id_masuk=%s"
        aksiCur.execute(sql, (id_masuk,))
        data = aksiCur.fetchone()
        aksiCur.close()
        return data

    # ===================== SIMPAN =====================
    def simpanDataBarangMasuk(self, id_barang, tanggal, jumlah, id_user):
        aksiCur = self.koneksi.cursor()
        sql = "INSERT INTO barang_masuk (id_barang, tanggal, jumlah, id_user) VALUES (%s, %s, %s, %s)"
        aksiCur.execute(sql, (id_barang, tanggal, jumlah, id_user))
        self.koneksi.commit()
        aksiCur.close()

    # ===================== UBAH =====================
    def ubahDataBarangMasuk(self, id_barang, tanggal, jumlah, id_user, id_masuk):
        aksiCur = self.koneksi.cursor()
        sql = "UPDATE barang_masuk SET id_barang=%s, tanggal=%s, jumlah=%s, id_user=%s WHERE id_masuk=%s"
        aksiCur.execute(sql, (id_barang, tanggal, jumlah, id_user, id_masuk))
        self.koneksi.commit()
        aksiCur.close()

    # ===================== HAPUS =====================
    def hapusDataBarangMasuk(self, id_masuk):
        aksiCur = self.koneksi.cursor()
        sql = "DELETE FROM barang_masuk WHERE id_masuk=%s"
        aksiCur.execute(sql, (id_masuk,))
        self.koneksi.commit()
        aksiCur.close()

    def laporanBarangMasuk(self):
        aksiCur = self.koneksi.cursor()
        aksiCur.execute("select * From barang_masuk")
        datalist = aksiCur.fetchall()

        tabel_data = [["id_masuk", "id_barang", "tanggal", "jumlah", "id_user"]] + list(datalist)

        pdffile = "laporan_barang_masuk.pdf"
        doc = SimpleDocTemplate(pdffile, pagesize=landscape(A4))
        tabel = Table(tabel_data, colWidths=[50, 100, 100, 100, 100])

        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ])
        tabel.setStyle(style)

        doc.build([tabel])
        aksiCur.close()
        print(f"Laporan berhasil dibuat: {pdffile}")
