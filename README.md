# UTS Visual 3 - Rudy 2310010148

Proyek aplikasi manajemen inventaris perkantoran menggunakan PySide6 dan MySQL untuk mata kuliah Visual 3.

## Deskripsi

Aplikasi ini adalah sistem manajemen inventaris yang dibangun dengan PySide6 (Qt for Python) dan MySQL. Aplikasi ini memungkinkan pengguna untuk mengelola data barang, transaksi barang masuk, barang keluar, dan data instansi.

## Fitur

- **Manajemen Data Barang**: CRUD (Create, Read, Update, Delete) untuk data barang.
- **Transaksi Barang Masuk**: Pencatatan barang yang masuk ke gudang.
- **Transaksi Barang Keluar**: Pencatatan barang yang keluar dari gudang.
- **Manajemen Instansi**: CRUD untuk data instansi.
- **Autentikasi Pengguna**: Sistem login untuk pengguna.
- **Interface GUI**: Antarmuka pengguna berbasis Qt Designer.

## Persyaratan

- Python 3.8 atau lebih baru
- PySide6
- mysql-connector-python
- MySQL Server

## Instalasi

1. Clone repository ini:
   ```bash
   git clone https://github.com/rudy0317/UTS_Visual3_Rudy_2310010148.git
   cd UTS_Visual3_Rudy_2310010148
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Setup database:
   - Import file `config/dbvisual3_2310010148.sql` ke MySQL server Anda.
   - Sesuaikan konfigurasi database di `config/db_config.py`.

## Penggunaan

1. Jalankan aplikasi:
   ```bash
   python main.py
   ```

2. Login dengan kredensial yang tersedia (lihat data di database).

3. Akses menu untuk mengelola data barang, transaksi, dan instansi.

## Struktur Proyek

- `config/`: Konfigurasi database
- `database/`: Koneksi database dan file SQL
- `models/`: Model data untuk interaksi dengan database
- `views/`: View dan form GUI
- `ui/`: File UI dari Qt Designer
- `main.py`: Entry point aplikasi

## Kontribusi

Untuk kontribusi, silakan buat pull request atau issue di repository ini.

## Lisensi

Proyek ini dibuat untuk keperluan akademik UTS Visual 3.
