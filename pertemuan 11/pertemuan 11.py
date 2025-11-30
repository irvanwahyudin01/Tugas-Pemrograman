print("PROGRAM INPUT NILAI MAHASISWA\n\n")
data_mahasiswa = {}

# fungsi menambahkan data
def tambah():
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    tugas = int(input("Masukkan Nilai Tugas: "))
    uts = int(input("Masukkan Nilai UTS: "))
    uas = int(input("Masukkan Nilai UAS: "))
    akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
    data_mahasiswa[nama] = {
            "nim": nim,
            "tugas": tugas,
            "uts": uts,
            "uas": uas,
            "akhir": akhir
        }
    print("Data Mahasiswa berhasil ditambahkan!")

# fungsi menampilkan data
def tampilkan():
    print("========================================================================")
    print(f"{('| No').ljust(5)}| {('Nama').ljust(20)}| {('Nim').ljust(10)}| {('Tugas').ljust(6)}| {('UTS').ljust(6)}| {('UAS').ljust(6)}| {('AKHIR').ljust(6)}|")
    print("------------------------------------------------------------------------")
    if not data_mahasiswa:
        print("|                    TIDAK ADA DATA MAHASISWA                          |")
    else:
        no = 1
        for nama, i in data_mahasiswa.items():
            print(f"{('| %d'%no).ljust(5)}| {str(nama).ljust(20)}| {(i['nim']).ljust(10)}| {str(i['tugas']).ljust(6)}| {str(i['uts']).ljust(6)}| {str(i['uas']).ljust(6)}| {str('%d'%i['akhir']).ljust(6)}|",end="\n")
            no += 1
    print("===============================================================================================")

# fungsi mengubah data berdasarkan nama
def ubah(nama):
    if nama in data_mahasiswa:
        print("Data ditemukan. Silakan masukkan data baru.")
        nim = input("Masukan Nim: ")
        tugas = int(input("Masukkan Nilai Tugas: "))
        uts = int(input("Masukkan Nilai UTS: "))
        uas = int(input("Masukkan Nilai UAS: "))
        akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
        data_mahasiswa[nama] = {
            "nim": nim,
            "tugas": tugas,
            "uts": uts,
            "uas": uas,
            "akhir": akhir
        }
        print("Data Mahasiswa berhasil diubah!")
    else:
        print("Maaf, Data dengan NAMA tersebut tidak ditemukan. Periksa kembali NAMA Mahasiswa")

# fungsi menghapus data berdasarkan nama
def hapus(cnama):
    if cnama in data_mahasiswa:
        del data_mahasiswa[cnama]
        print("Data berhasil dihapus!")
    else:
        print("Tidak ada data yang ditemukan")
# fungsi cari data berdasarkan nama
def cari(cnama):
    if cnama in data_mahasiswa:
        mhs = data_mahasiswa[cnama]
        print("\nData Mahasiswa:")
        print(f"NIM         : {mhs['nim']}")
        print(f"Nama        : {cnama}")
        print(f"Tugas       : {mhs['tugas']}")
        print(f"UTS         : {mhs['uts']}")
        print(f"UAS         : {mhs['uas']}")
        print(f"Nilai Akhir : {mhs['akhir']}")
    else:
        print("Data yang input tidak ditemukan")

# membuat kondisi dan memangil fungsi
while True:
    pilih=input("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar] : ")
    if pilih == 'T':
        tambah()
    elif pilih == 'L':
        tampilkan()
    elif pilih == 'U':
        cnama = input("Masukkan NAMA Mahasiswa yang akan diubah: ")
        ubah(cnama)
    elif pilih == 'H':
        cnama = input("Masukkan NAMA yang akan dihapus: ")
        hapus(cnama)
    elif pilih == 'C':
        cnama = input("Masukkan NAMA yang dicari: ")
        cari(cnama)
    elif pilih == 'K':
        print("Terima kasih telah menggunakan program ini.")
        break
