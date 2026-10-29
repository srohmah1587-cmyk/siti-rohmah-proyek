
# PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA KELAS

**Nama:** Siti Rohmah  
**NIM:** 2225250203  
**Kelas:** 3A  

## 1. Deskripsi Program

Program Rekap dan Analisis Nilai Matematika Kelas merupakan aplikasi sederhana berbasis Python yang digunakan untuk membaca, memvalidasi, mengolah, dan menampilkan data nilai siswa.

Program ini membantu proses rekapitulasi nilai dengan menghitung jumlah siswa, total nilai, rata-rata, nilai tertinggi, nilai terendah, serta jumlah siswa yang tuntas dan belum tuntas.

Batas ketuntasan yang digunakan adalah 60. Siswa dinyatakan tuntas apabila memperoleh nilai minimal 60.

## 2. Tujuan Program

Tujuan pembuatan program ini adalah:

1. Membaca data nilai siswa dari file teks.
2. Memvalidasi data agar hanya nilai yang benar yang diproses.
3. Menghitung statistik nilai siswa.
4. Menentukan status ketuntasan siswa.
5. Menampilkan dan menyimpan hasil rekap nilai.
6. Menerapkan penggunaan fungsi, modul, percabangan, perulangan, dan pengolahan file dalam Python.

## 3. Fitur Program

Fitur yang tersedia meliputi:

- Membaca data siswa dari file teks.
- Memeriksa NIM dan nilai siswa.
- Menolak nilai yang bukan angka atau berada di luar rentang 0–100.
- Menghindari pemrosesan NIM yang duplikat.
- Menghitung total dan rata-rata nilai.
- Menentukan nilai tertinggi dan terendah.
- Mengelompokkan siswa berdasarkan ketuntasan.
- Menampilkan hasil analisis di terminal.
- Menyimpan rekap ke dalam file teks.

## 4. Struktur Folder

```text
proyek_nilai/
├── main.py
├── input_data.py
├── data_io.py
├── analisis.py
├── proses.py
├── utilitas.py
├── output.py
├── proposal.md
├── test_case.md
├── README.md
├── .gitignore
├── data/
│   └── contoh_data.txt
└── output/
    └── .gitkeep
```

**Keterangan fungsi file:**

| File | Fungsi |
|---|---|
| `main.py` | Menjalankan program utama |
| `input_data.py` | Menerima input NIM dan nilai siswa |
| `data_io.py` | Membaca dan menyimpan data |
| `analisis.py` | Menghitung statistik dan ketuntasan |
| `proses.py` | Memvalidasi dan memproses data |
| `utilitas.py` | Menyediakan fungsi validasi dan format |
| `output.py` | Menampilkan dan menyimpan hasil rekap |
| `contoh_data.txt` | Menyimpan data contoh siswa |
| `test_case.md` | Mendokumentasikan pengujian program |
| `proposal.md` | Menjelaskan rencana dan rancangan program |
| `.gitignore` | Mengatur file yang tidak perlu dilacak Git |

## 5. Format Data Masukan

Data masukan disimpan di `data/contoh_data.txt`. Setiap baris menggunakan format:

```text
NIM,nilai
```

Contoh isi file:

```text
A001,85
A002,78
A003,92
A004,abc
A005,60
A006,50
A007,75
A008,88
A009,45
A010,100
```

Data `A004,abc` sengaja disertakan untuk menguji validasi nilai yang tidak valid.

## 6. Ketentuan Pengolahan Nilai

Ketentuan yang digunakan dalam program adalah:

1. Nilai harus berupa angka antara 0 sampai 100.
2. NIM tidak boleh kosong atau duplikat.
3. Nilai minimal 60 dinyatakan **Tuntas**.
4. Nilai di bawah 60 dinyatakan **Belum Tuntas**.
5. Data yang tidak valid tidak dimasukkan dalam perhitungan statistik.
6. Jika file tidak ditemukan atau tidak dapat dibaca, program menampilkan pesan kesalahan.

## 7. Cara Menjalankan Program

Pastikan Python telah terpasang di komputer.

Buka terminal pada folder utama proyek, kemudian jalankan:

```bash
python main.py
```

Pada beberapa sistem, gunakan:

```bash
python3 main.py
```

Pastikan `main.py` membaca file yang benar, yaitu `data/contoh_data.txt`, dan memanggil fungsi pengolahan serta output sesuai nama modul yang digunakan.

## 8. Contoh Hasil Pengujian

Berdasarkan data contoh, satu baris tidak valid, yaitu `A004,abc`. Dengan demikian, terdapat 9 data siswa valid.

| Komponen | Hasil |
|---|---:|
| Jumlah siswa valid | 9 |
| Total nilai | 673 |
| Rata-rata nilai | 74,78 |
| Nilai tertinggi | 100 |
| Nilai terendah | 45 |
| Siswa tuntas | 7 |
| Siswa belum tuntas | 2 |
| Data tidak valid | 1 |

Siswa yang tuntas adalah A001, A002, A003, A005, A007, A008, dan A010. Siswa yang belum tuntas adalah A006 dan A009.

## 9. Pengujian Program

Pengujian dilakukan untuk memastikan program berjalan sesuai ketentuan.

| No. | Skenario Pengujian | Hasil yang Diharapkan |
|---:|---|---|
| 1 | Memasukkan nilai 85 | Data diterima dan berstatus tuntas |
| 2 | Memasukkan nilai 60 | Data diterima dan berstatus tuntas |
| 3 | Memasukkan nilai 45 | Data diterima dan berstatus belum tuntas |
| 4 | Memasukkan nilai `abc` | Data ditolak |
| 5 | Memasukkan nilai 120 | Data ditolak |
| 6 | Memasukkan NIM duplikat | Data duplikat ditolak |
| 7 | Membaca file yang tidak ditemukan | Pesan kesalahan ditampilkan |
| 8 | Menyimpan hasil rekap | File rekap dibuat jika penyimpanan berhasil |

## 10. Analisis Efisiensi

Misalkan \(n\) adalah jumlah data siswa yang diproses.

Proses pembacaan dan pengolahan data dilakukan dengan menelusuri setiap data satu kali. Perhitungan total, rata-rata, nilai tertinggi, nilai terendah, dan status ketuntasan memiliki kompleksitas waktu keseluruhan sekitar **O(n)**, dengan asumsi validasi dan operasi per data berlangsung dalam waktu konstan.

Penyimpanan data memerlukan ruang tambahan sekitar **O(n)** karena data siswa disimpan dalam struktur list untuk diproses.

## 11. Kesimpulan

Program ini membantu proses rekapitulasi dan analisis nilai matematika siswa secara lebih terstruktur. Program menerapkan validasi data, perhitungan statistik, penentuan ketuntasan, serta penyimpanan hasil ke file teks.

Melalui proyek ini, konsep dasar pemrograman Python dapat diterapkan dalam penyelesaian masalah pengolahan data nilai siswa.