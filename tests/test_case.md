
# TEST CASE
## Program Rekap dan Analisis Nilai Matematika Kelas

**Nama:** Siti Rohmah  
**NIM:** 2225250203  
**Kelas:** 3A  

---

## 1. Tujuan Pengujian

Pengujian dilakukan untuk memastikan bahwa program rekap dan analisis nilai matematika kelas dapat berjalan dengan benar. Pengujian mencakup pembacaan data dari file, validasi nilai, perhitungan statistik, penentuan status ketuntasan, dan penanganan data yang tidak valid.

## 2. Ketentuan Program

- Nilai siswa berada pada rentang 0 sampai 100.
- Batas ketuntasan adalah 60.
- Siswa dengan nilai lebih besar atau sama dengan 60 dinyatakan **Tuntas**.
- Siswa dengan nilai kurang dari 60 dinyatakan **Belum Tuntas**.
- Baris data yang tidak valid tidak dimasukkan ke dalam perhitungan.
- Jika tidak terdapat data yang valid, program menampilkan pesan bahwa data tidak tersedia.

## 3. Data Pengujian

Isi file `data/nilai_contoh.txt`:

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

Keterangan: Data A004 tidak valid karena nilai berisi teks `abc`.

## 4. Daftar Test Case

| ID | Skenario Pengujian | Data Masukan | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Nilai di atas batas ketuntasan | 85 | Status Tuntas |
| TC02 | Nilai tepat pada batas ketuntasan | 60 | Status Tuntas |
| TC03 | Nilai di bawah batas ketuntasan | 45 | Status Belum Tuntas |
| TC04 | Nilai minimum yang valid | 0 | Nilai diterima |
| TC05 | Nilai maksimum yang valid | 100 | Nilai diterima |
| TC06 | Nilai di bawah rentang | -5 | Nilai ditolak |
| TC07 | Nilai di atas rentang | 110 | Nilai ditolak |
| TC08 | Nilai berupa teks | abc | Data ditolak dan dilewati |
| TC09 | Data siswa lengkap dan valid | NIM dan nilai dipisahkan koma | Data dibaca dengan benar |
| TC10 | Baris tanpa pemisah koma | A011 80 | Baris ditolak |
| TC11 | Baris kosong | Baris kosong dalam file | Baris dilewati |
| TC12 | File tidak ditemukan | Nama file yang tidak tersedia | Pesan kesalahan ditampilkan |
| TC13 | Tidak ada data valid | File kosong atau seluruh data tidak valid | Pesan bahwa data tidak tersedia |
| TC14 | Menghitung rata-rata | Nilai 80, 70, 90 | Rata-rata 80 |
| TC15 | Menentukan nilai tertinggi | Nilai 80, 70, 90 | Nilai tertinggi 90 |
| TC16 | Menentukan nilai terendah | Nilai 80, 70, 90 | Nilai terendah 70 |
| TC17 | Menghitung jumlah siswa tuntas | Nilai 60, 75, 50 | 2 siswa tuntas |
| TC18 | Menghitung jumlah siswa belum tuntas | Nilai 60, 75, 50 | 1 siswa belum tuntas |
| TC19 | Menampilkan hasil rekap | Data nilai valid | Ringkasan statistik ditampilkan |
| TC20 | Menyimpan hasil rekap | Data nilai valid | File hasil rekap dibuat dan berisi ringkasan |

## 5. Hasil Perhitungan yang Diharapkan

Berdasarkan data pengujian pada bagian 3, terdapat sembilan data nilai yang valid.

| Komponen | Hasil yang Diharapkan |
|---|---:|
| Jumlah data valid | 9 siswa |
| Total nilai | 673 |
| Rata-rata nilai | 74,78 |
| Nilai tertinggi | 100 |
| Nilai terendah | 45 |
| Jumlah siswa tuntas | 7 siswa |
| Jumlah siswa belum tuntas | 2 siswa |
| Jumlah data tidak valid | 1 data |

## 6. Pengujian Fungsi Utilitas

| ID | Fungsi | Masukan | Hasil yang Diharapkan |
|---|---|---|---|
| UT01 | `validasi_nilai()` | 80 | `True` |
| UT02 | `validasi_nilai()` | 120 | `False` |
| UT03 | `validasi_nilai()` | `"abc"` | `False` |
| UT04 | `status_ketuntasan()` | 85 | `"Tuntas"` |
| UT05 | `status_ketuntasan()` | 60 | `"Tuntas"` |
| UT06 | `status_ketuntasan()` | 45 | `"Belum Tuntas"` |
| UT07 | `format_nilai()` | 85 | `"85.00"` |
| UT08 | `format_nilai()` | `"abc"` | `"Tidak valid"` |

## 7. Pengujian Perhitungan Analisis

| ID | Fungsi | Masukan | Hasil yang Diharapkan |
|---|---|---|---|
| AN01 | `analisis_nilai()` | Nilai 80, 70, 90 | Rata-rata 80 |
| AN02 | `analisis_nilai()` | Data kosong | Mengembalikan `None` |
| AN03 | `analisis_nilai()` | Nilai 60 dan 50 | 1 siswa tuntas dan 1 belum tuntas |
| AN04 | `analisis_nilai()` | Nilai 100 dan 0 | Nilai tertinggi 100 dan terendah 0 |

## 8. Kriteria Keberhasilan

Pengujian dinyatakan berhasil apabila:

1. Program dapat membaca data dari file yang tersedia.
2. Data tidak valid dapat ditangani tanpa menghentikan seluruh program.
3. Nilai di luar rentang 0–100 ditolak.
4. Perhitungan rata-rata, nilai tertinggi, dan nilai terendah sesuai dengan hasil yang diharapkan.
5. Status ketuntasan ditentukan menggunakan batas nilai 60.
6. Program dapat menangani file yang tidak ditemukan dan data kosong.
7. Hasil rekap dapat ditampilkan dan disimpan sesuai fungsi program.

## 9. Kesimpulan

Test case ini digunakan sebagai pedoman untuk memeriksa ketepatan dan keandalan Program Rekap dan Analisis Nilai Matematika Kelas. Program dinyatakan memenuhi kebutuhan apabila seluruh pengujian berjalan sesuai hasil yang diharapkan. Hasil aktual setiap pengujian perlu dicatat setelah program dijalankan.