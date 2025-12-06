class MahasiswaManager:
    def __init__(self):
        self.data = {}

    # Method tambah()
    def tambah(self):
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        tugas = int(input("Masukkan Nilai Tugas: "))
        uts = int(input("Masukkan Nilai UTS: "))
        uas = int(input("Masukkan Nilai UAS: "))
        akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

        self.data[nama] = {
            "nim": nim,
            "tugas": tugas,
            "uts": uts,
            "uas": uas,
            "akhir": akhir
        }
        print("Data Mahasiswa berhasil ditambahkan!\n")

    # Method tampilkan()
    def tampilkan(self):
        print("========================================================================")
        print(f"{'No':<5} {'Nama':<20} {'NIM':<10} {'Tugas':<6} {'UTS':<6} {'UAS':<6} {'Akhir':<6}")
        print("------------------------------------------------------------------------")

        if not self.data:
            print("                     TIDAK ADA DATA MAHASISWA")
        else:
            for i, (nama, mhs) in enumerate(self.data.items(), start=1):
                print(f"{i:<5} {nama:<20} {mhs['nim']:<10} {mhs['tugas']:<6} {mhs['uts']:<6} {mhs['uas']:<6} {mhs['akhir']:<6.2f}")

        print("========================================================================\n")

    # Method ubah(nama)
    def ubah(self, nama):
        if nama in self.data:
            print("Data ditemukan, masukkan data baru.")
            nim = input("Masukkan NIM baru: ")
            tugas = int(input("Masukkan Nilai Tugas baru: "))
            uts = int(input("Masukkan Nilai UTS baru: "))
            uas = int(input("Masukkan Nilai UAS baru: "))
            akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

            self.data[nama] = {
                "nim": nim,
                "tugas": tugas,
                "uts": uts,
                "uas": uas,
                "akhir": akhir
            }
            print("Data berhasil diubah!\n")
        else:
            print("Data tidak ditemukan!\n")

    # Method hapus(nama)
    def hapus(self, nama):
        if nama in self.data:
            del self.data[nama]
            print("Data berhasil dihapus!\n")
        else:
            print("Data tidak ditemukan!\n")


# === MAIN PROGRAM ===
manager = MahasiswaManager()

while True:
    menu = input("[(L)ihat, (T)ambah, (U)bah, (H)apus, (K)eluar] : ")

    if menu.upper() == "T":
        manager.tambah()
    elif menu.upper() == "L":
        manager.tampilkan()
    elif menu.upper() == "U":
        nama = input("Masukkan nama yang akan diubah: ")
        manager.ubah(nama)
    elif menu.upper() == "H":
        nama = input("Masukkan nama yang akan dihapus: ")
        manager.hapus(nama)
    elif menu.upper() == "K":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")
