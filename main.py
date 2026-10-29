
# Program Rekap dan Analisis Nilai Matematika Kelas
# Nama  : Siti Rohmah
# NIM   : 2225250203
# Kelas : 3A

from pathlib import Path


BATAS_KETUNTASAN = 60


def baca_nilai(nama_file):
    """Membaca dan memvalidasi data nilai dari file."""
    data_nilai = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor_baris, baris in enumerate(file, start=1):
                baris = baris.strip()

                if not baris:
                    continue

                bagian = baris.split(",")

                if len(bagian) != 2:
                    print(
                        f"Peringatan: Format salah pada baris "
                        f"{nomor_baris}."
                    )
                    continue

                nim = bagian[0].strip()

                try:
                    nilai = float(bagian[1].strip())
                except ValueError:
                    print(
                        f"Peringatan: Nilai bukan angka pada baris "
                        f"{nomor_baris}."
                    )
                    continue

                if not nim or not 0 <= nilai <= 100:
                    print(
                        f"Peringatan: Data tidak valid pada baris "
                        f"{nomor_baris}."
                    )
                    continue

                data_nilai.append((nim, nilai))

    except FileNotFoundError:
        print(f"Error: File '{nama_file}' tidak ditemukan.")
        return None

    return data_nilai


def analisis_nilai(data_nilai):
    """Menghitung statistik dan status ketuntasan nilai."""
    if not data_nilai:
        return None

    nilai_siswa = [nilai for nim, nilai in data_nilai]

    jumlah_siswa = len(nilai_siswa)
    rata_rata = sum(nilai_siswa) / jumlah_siswa
    nilai_tertinggi = max(nilai_siswa)
    nilai_terendah = min(nilai_siswa)
    jumlah_tuntas = sum(
        1 for nilai in nilai_siswa
        if nilai >= BATAS_KETUNTASAN
    )
    jumlah_belum_tuntas = jumlah_siswa - jumlah_tuntas

    return {
        "jumlah_siswa": jumlah_siswa,
        "rata_rata": rata_rata,
        "nilai_tertinggi": nilai_tertinggi,
        "nilai_terendah": nilai_terendah,
        "jumlah_tuntas": jumlah_tuntas,
        "jumlah_belum_tuntas": jumlah_belum_tuntas,
    }


def tampilkan_hasil(data_nilai, hasil):
    """Menampilkan detail nilai dan hasil analisis."""
    print("\nPROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA KELAS")
    print("=" * 52)

    print("\nDETAIL NILAI SISWA")
    print("-" * 52)
    print(f"{'NIM':<12}{'Nilai':<12}{'Status'}")
    print("-" * 52)

    for nim, nilai in data_nilai:
        if nilai >= BATAS_KETUNTASAN:
            status = "Tuntas"
        else:
            status = "Belum tuntas"

        print(f"{nim:<12}{nilai:<12g}{status}")

    print("\nHASIL ANALISIS NILAI")
    print("-" * 52)
    print(f"Jumlah siswa valid   : {hasil['jumlah_siswa']}")
    print(f"Rata-rata kelas      : {hasil['rata_rata']:.2f}")
    print(f"Nilai tertinggi      : {hasil['nilai_tertinggi']:g}")
    print(f"Nilai terendah       : {hasil['nilai_terendah']:g}")
    print(f"Jumlah siswa tuntas  : {hasil['jumlah_tuntas']}")
    print(
        f"Jumlah belum tuntas  : "
        f"{hasil['jumlah_belum_tuntas']}"
    )
    print(f"Batas ketuntasan     : {BATAS_KETUNTASAN}")


def main():
    """Menjalankan program utama."""
    folder_proyek = Path(__file__).resolve().parent
    lokasi_file = folder_proyek / "data" / "nilai_contoh.txt"

    data_nilai = baca_nilai(lokasi_file)

    if data_nilai is None:
        return

    hasil = analisis_nilai(data_nilai)

    if hasil is None:
        print("Tidak ada data nilai yang valid untuk dianalisis.")
        return

    tampilkan_hasil(data_nilai, hasil)


if __name__ == "__main__":
    main()