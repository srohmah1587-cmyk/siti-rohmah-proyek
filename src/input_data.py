
# Nama: Siti Rohmah
# NIM: 2225250203
# Kelas: 3A
# File: input_data.py
# Program Rekap dan Analisis Nilai Matematika Kelas

from utilitas import validasi_nilai


def input_data_siswa():
    """
    Menerima data NIM dan nilai siswa melalui terminal.

    Pengguna dapat memasukkan beberapa data siswa.
    Input dihentikan jika pengguna mengetik 'selesai'
    pada bagian NIM.
    """

    data_nilai = []

    print("\n=== INPUT DATA NILAI SISWA ===")
    print("Masukkan NIM dan nilai siswa.")
    print("Ketik 'selesai' pada bagian NIM untuk mengakhiri input.")

    while True:
        nim = input("\nMasukkan NIM siswa: ").strip()

        if nim.lower() == "selesai":
            break

        if not nim:
            print("NIM tidak boleh kosong.")
            continue

        try:
            nilai = float(input("Masukkan nilai siswa (0-100): ").strip())
        except ValueError:
            print("Input nilai harus berupa angka.")
            continue

        if not validasi_nilai(nilai):
            print("Nilai harus berada pada rentang 0 sampai 100.")
            continue

        # Memeriksa apakah NIM sudah pernah dimasukkan
        if any(nim_lama == nim for nim_lama, _ in data_nilai):
            print("NIM tersebut sudah dimasukkan.")
            continue

        data_nilai.append((nim, nilai))
        print("Data siswa berhasil ditambahkan.")

    print(f"\nJumlah data yang berhasil dimasukkan: {len(data_nilai)}")
    return data_nilai


def tampilkan_data_input(data_nilai):
    """Menampilkan data siswa yang sudah dimasukkan."""

    if not data_nilai:
        print("Belum ada data siswa yang dimasukkan.")
        return

    print("\n=== DAFTAR DATA NILAI SISWA ===")
    print(f"{'NIM':<15}{'NILAI':>10}")
    print("-" * 25)

    for nim, nilai in data_nilai:
        print(f"{nim:<15}{nilai:>10.2f}")

    print("-" * 25)


if __name__ == "__main__":
    data = input_data_siswa()
    tampilkan_data_input(data)