
# Nama: Siti Rohmah
# NIM: 2225250203
# Kelas: 3A
# File: output.py
# Program Rekap dan Analisis Nilai Matematika Kelas

from pathlib import Path


def tampilkan_output(hasil):
    """Menampilkan hasil rekap nilai siswa ke terminal."""

    if not hasil or hasil["jumlah_siswa"] == 0:
        print("\nTidak ada data nilai yang dapat ditampilkan.")
        return

    print("\n" + "=" * 60)
    print("REKAP DAN ANALISIS NILAI MATEMATIKA KELAS".center(60))
    print("=" * 60)

    print(f"{'NIM':<15}{'NILAI':>12}{'STATUS':>20}")
    print("-" * 60)

    for siswa in hasil["data"]:
        print(
            f"{siswa['nim']:<15}"
            f"{siswa['nilai']:>12.2f}"
            f"{siswa['status']:>20}"
        )

    print("-" * 60)
    print("\nRINGKASAN NILAI")
    print("-" * 30)
    print(f"Jumlah siswa valid    : {hasil['jumlah_siswa']}")
    print(f"Total nilai           : {hasil['total_nilai']:.2f}")
    print(f"Rata-rata nilai       : {hasil['rata_rata']:.2f}")

    if hasil["nilai_tertinggi"] is not None:
        print(f"Nilai tertinggi       : {hasil['nilai_tertinggi']:.2f}")
        print(f"Nilai terendah        : {hasil['nilai_terendah']:.2f}")
    else:
        print("Nilai tertinggi       : Tidak tersedia")
        print("Nilai terendah        : Tidak tersedia")

    print(f"Siswa tuntas          : {hasil['jumlah_tuntas']}")
    print(f"Siswa belum tuntas    : {hasil['jumlah_belum_tuntas']}")
    print(f"Data tidak valid      : {len(hasil['data_tidak_valid'])}")
    print("=" * 60)


def simpan_output(hasil, nama_file="output/hasil_rekap.txt"):
    """Menyimpan hasil rekap nilai ke dalam file teks."""

    if not hasil:
        print("Rekap tidak dapat disimpan karena hasil tidak tersedia.")
        return

    lokasi_file = Path(nama_file)

    try:
        lokasi_file.parent.mkdir(parents=True, exist_ok=True)

        with open(lokasi_file, "w", encoding="utf-8") as file:
            file.write("REKAP DAN ANALISIS NILAI MATEMATIKA KELAS\n")
            file.write("=" * 50 + "\n\n")

            file.write("DAFTAR NILAI SISWA\n")
            file.write("-" * 50 + "\n")
            file.write(f"{'NIM':<15}{'NILAI':>12}{'STATUS':>20}\n")
            file.write("-" * 50 + "\n")

            for siswa in hasil["data"]:
                file.write(
                    f"{siswa['nim']:<15}"
                    f"{siswa['nilai']:>12.2f}"
                    f"{siswa['status']:>20}\n"
                )

            file.write("\nRINGKASAN NILAI\n")
            file.write("-" * 30 + "\n")
            file.write(f"Jumlah siswa valid    : {hasil['jumlah_siswa']}\n")
            file.write(f"Total nilai           : {hasil['total_nilai']:.2f}\n")
            file.write(f"Rata-rata nilai       : {hasil['rata_rata']:.2f}\n")

            if hasil["nilai_tertinggi"] is not None:
                file.write(
                    f"Nilai tertinggi       : "
                    f"{hasil['nilai_tertinggi']:.2f}\n"
                )
                file.write(
                    f"Nilai terendah        : "
                    f"{hasil['nilai_terendah']:.2f}\n"
                )
            else:
                file.write("Nilai tertinggi       : Tidak tersedia\n")
                file.write("Nilai terendah        : Tidak tersedia\n")

            file.write(f"Siswa tuntas          : {hasil['jumlah_tuntas']}\n")
            file.write(
                f"Siswa belum tuntas    : "
                f"{hasil['jumlah_belum_tuntas']}\n"
            )
            file.write(
                f"Data tidak valid      : "
                f"{len(hasil['data_tidak_valid'])}\n"
            )

            if hasil["data_tidak_valid"]:
                file.write("\nDATA YANG DITOLAK\n")
                file.write("-" * 30 + "\n")

                for item in hasil["data_tidak_valid"]:
                    file.write(
                        f"Baris {item['baris']}: {item['alasan']}\n"
                    )

        print(f"\nRekap berhasil disimpan di: {lokasi_file}")

    except OSError as error:
        print(f"Gagal menyimpan rekap: {error}")


if __name__ == "__main__":
    print("File output.py berisi fungsi untuk menampilkan dan menyimpan rekap.")
    print("Jalankan melalui main.py agar terhubung dengan data nilai siswa.")