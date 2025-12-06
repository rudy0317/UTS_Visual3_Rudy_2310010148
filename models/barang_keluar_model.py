# models/barang_keluar_model.py
from database.connection import get_connection
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

class BarangKeluarModel:
    def __init__(self):
        self.conn = get_connection()

    # ===================== TAMPIL DATA =====================
    def dataBarangKeluar(self):
        cur = self.conn.cursor(dictionary=True)
        sql = """
            SELECT
                bk.id_keluar,
                b.kode,
                b.nama,
                bk.tanggal,
                bk.jumlah,
                u.nama AS nama_user
            FROM barang_keluar bk
            LEFT JOIN data_barang b ON b.id_barang = bk.id_barang
            LEFT JOIN users u ON u.id_user = bk.id_user
            ORDER BY bk.id_keluar DESC
        """
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        return rows

    # ===================== FILTER DATA =====================
    def filterBarangKeluar(self, kata):
        cur = self.conn.cursor(dictionary=True)
        pattern = f"%{kata}%"
        sql = """
            SELECT
                bk.id_keluar,
                b.kode,
                b.nama,
                bk.tanggal,
                bk.jumlah,
                u.nama AS nama_user
            FROM barang_keluar bk
            LEFT JOIN data_barang b ON b.id_barang = bk.id_barang
            LEFT JOIN users u ON u.id_user = bk.id_user
            WHERE b.kode LIKE %s
            OR b.nama LIKE %s
            OR u.nama LIKE %s
            ORDER BY bk.id_keluar DESC
        """
        cur.execute(sql, (pattern, pattern, pattern))
        rows = cur.fetchall()
        cur.close()
        return rows

    # ===================== SIMPAN =====================
    def simpanDataBarangKeluar(self, id_barang, tanggal, jumlah, id_user):
        cur = self.conn.cursor()
        sql = """
            INSERT INTO barang_keluar (id_barang, tanggal, jumlah, id_user)
            VALUES (%s, %s, %s, %s)
        """
        cur.execute(sql, (id_barang, tanggal, jumlah, id_user))
        self.conn.commit()
        cur.close()

    # ===================== UBAH =====================
    def ubahDataBarangKeluar(self, id_barang, tanggal, jumlah, id_user, id_keluar):
        cur = self.conn.cursor()
        sql = """
            UPDATE barang_keluar
            SET id_barang = %s,
                tanggal   = %s,
                jumlah    = %s,
                id_user   = %s
            WHERE id_keluar = %s
        """
        cur.execute(sql, (id_barang, tanggal, jumlah, id_user, id_keluar))
        self.conn.commit()
        cur.close()

    # ===================== HAPUS =====================
    def hapusDataBarangKeluar(self, id_keluar):
        cur = self.conn.cursor()
        sql = "DELETE FROM barang_keluar WHERE id_keluar = %s"
        cur.execute(sql, (id_keluar,))
        self.conn.commit()
        cur.close()

    def laporanBarangKeluar(self):
        aksiCur = self.conn.cursor()
        aksiCur.execute("select * From barang_keluar")
        datalist = aksiCur.fetchall()

        tabel_data = [["id_keluar", "id_barang", "tanggal", "jumlah", "id_user"]] + list(datalist)

        pdffile = "laporan_barang_keluar.pdf"
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
