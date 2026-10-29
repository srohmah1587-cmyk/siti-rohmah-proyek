
# Nama: Siti Rohmah
# NIM: 2225250203
# Kelas: 3A
# File: proses.py
# Program Rekap dan Analisis Nilai Matematika Kelas

from utilitas import validasi_nilai, status_ketuntasan

BATAS_KETUNTASAN = 60


def proses_data_nilai(data_nilai, batas=BATAS_KETUNTASAN):
    """
    Memvalidasi dan memproses data nilai siswa.

    Parameter:
        data_nilai: daftar tuple (NIM, nilai)
        batas: nilai minimum untuk dinyatakan tuntas

    Return:
        Dictionary berisi hasil pengolahan data.
    """

    data_valid = []
    data_tidak_valid = []
    nim_terdaftar = set()

    for nomor, data in enumerate(data_nilai, start=1):
        if not isinstance(data, (tuple, list)) or len(data) != 2:
            data_tidak_valid.append({
                "baris": nomor,
                "data": data,
                "alasan": "Format data harus berisi NIM dan nilai."
            })
            continue

        nim, nilai = data

        if not isinstance(nim, str) or not nim.strip():
            data_tidak_valid.append({
                "baris": nomor,
                "data": data,
                "alasan": "NIM kosong atau tidak valid."
            })
            continue

        nim = nim.strip()

        if nim in nim_terdaftar:
            data_tidak_valid.append({
                "baris": nomor,
                "data": data,
                "alasan": "NIM duplikat."
            })
            continue

        if not validasi_nilai(nilai):
            data_tidak_valid.append({
                "baris": nomor,
                "data": data,
                "alasan": "Nilai harus berupa angka antara 0 dan 100."
            })
            continue

        nilai = float(nilai)
        nim_terdaftar.add(nim)

        data_valid.append({
            "nim": nim,
            "nilai": nilai,
            "status": status_ketuntasan(nilai, batas)
        })

    if not data_valid:
        return {
            "data": [],
            "data_tidak_valid": data_tidak_valid,
            "jumlah_siswa": 0,
            "total_nilai": 0,
            "rata_rata": 0,
            "nilai_tertinggi": None,
            "nilai_terendah": None,
            "jumlah_tuntas": 0,
            "jumlah_belum_tuntas": 0
        }

    daftar_nilai = [siswa["nilai"] for siswa in data_valid]
    total_nilai = sum(daftar_nilai)

    jumlah_tuntas = sum(
        1 for siswa in data_valid
        if siswa["status"] == "Tuntas"
    )

    jumlah_belum_tuntas = sum(
        1 for siswa in data_valid
        if siswa["status"] == "Belum Tuntas"
    )

    return {
        "data": data_valid,
        "data_tidak_valid": data_tidak_valid,
        "jumlah_siswa": len(data_valid),
        "total_nilai": total_nilai,
        "rata_rata": total_nilai / len(data_valid),
        "nilai_tertinggi": max(daftar_nilai),
        "nilai_terendah": min(daftar_nilai),
        "jumlah_tuntas": jumlah_tuntas,
        "jumlah_belum_tuntas": jumlah_belum_tuntas
    }


def tampilkan_hasil_proses(hasil):
    """Menampilkan hasil pengolahan nilai siswa."""

    print("\n=== HASIL PROSES NILAI SISWA ===")
    print("-" * 65)
    print(f"{'NIM':<15}{'NILAI':>10}{'STATUS':>20}")
    print("-" * 65)

    for siswa in hasil["data"]:
        print(
            f"{siswa['nim']:<15}"
            f"{siswa['nilai']:>10.2f}"
            f"{siswa['status']:>20}"
        )

    print("-" * 65)

    print("\n=== RINGKASAN NILAI ===")
    print(f"Jumlah siswa valid    : {hasil['jumlah_siswa']}")
    print(f"Total nilai           : {hasil['total_nilai']:.2f}")
    print(f"Rata-rata             : {hasil['rata_rata']:.2f}")

    if hasil["jumlah_siswa"] > 0:
        print(f"Nilai tertinggi       : {hasil['nilai_tertinggi']:.2f}")
        print(f"Nilai terendah        : {hasil['nilai_terendah']:.2f}")
    else:
        print("Nilai tertinggi       : Tidak tersedia")
        print("Nilai terendah        : Tidak tersedia")

    print(f"Siswa tuntas          : {hasil['jumlah_tuntas']}")
    print(f"Siswa belum tuntas    : {hasil['jumlah_belum_tuntas']}")
    print(f"Data tidak valid      : {len(hasil['data_tidak_valid'])}")

    if hasil["data_tidak_valid"]:
        print("\n=== DATA YANG DITOLAK ===")
        for item in hasil["data_tidak_valid"]:
            print(
                f"Baris {item['baris']}: "
                f"{item['alasan']} Data: {item['data']}"
            )


if __name__ == "__main__":
    data_uji = [
        ("A001", 85),
        ("A002", 60),
        ("A003", 45),
        ("A004", "abc"),
        ("A005", 100),
        ("A001", 90)
    ]

    hasil_uji = proses_data_nilai(data_uji)
    tampilkan_hasil_proses(hasil_uji)