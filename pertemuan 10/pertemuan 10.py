print("PROGRAM INPUT NILAI MAHASISWA\n\n")
data_mahasiswa = {}

while True:
    pilih=input("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar] : ")


    if pilih == 'T':
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        tugas = int(input("Masukkan Nilai Tugas: "))
        uts = int(input("Masukkan Nilai UTS: "))
        uas = int(input("Masukkan Nilai UAS: "))
        akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
        data_mahasiswa[nim] = {
            "nama": nama,
            "tugas": tugas,
            "uts": uts,
            "uas": uas,
            "akhir": akhir
        }
        print("Data Mahasiswa berhasil ditambahkan!")

    elif pilih == 'L':
        print("========================================================================")
        print(f"{('| No').ljust(5)}| {('Nama').ljust(20)}| {('Nim').ljust(10)}| {('Tugas').ljust(6)}| {('UTS').ljust(6)}| {('UAS').ljust(6)}| {('AKHIR').ljust(6)}|")
        print("------------------------------------------------------------------------")
        if not data_mahasiswa:
            print("|                    TIDAK ADA DATA MAHASISWA                          |")
        else:
            no = 1
            for nim, i in data_mahasiswa.items():
                print(f"{('| %d'%no).ljust(5)}| {(i['nama']).ljust(20)}| {str(nim).ljust(10)}| {str(i['tugas']).ljust(6)}| {str(i['uts']).ljust(6)}| {str(i['uas']).ljust(6)}| {str('%d'%i['akhir']).ljust(6)}|",end="\n")
                no += 1
        print("===============================================================================================")

    elif pilih == 'U':
        nim = input("Masukkan NIM Mahasiswa yang akan diubah: ")
        if nim in data_mahasiswa:
            print("Data ditemukan. Silakan masukkan data baru.")
            nama = input("Masukkan Nama: ")
            tugas = int(input("Masukkan Nilai Tugas: "))
            uts = int(input("Masukkan Nilai UTS: "))
            uas = int(input("Masukkan Nilai UAS: "))
            nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
            data_mahasiswa[nim] = {
                "nama": nama,
                "tugas": tugas,
                "uts": uts,
                "uas": uas,
                "akhir": akhir
            }
            print("Data Mahasiswa berhasil diubah!")
        else:
            print("Maaf, Data dengan NIM tersebut tidak ditemukan. Periksa kembali NIM Mahasiswa")

    elif pilih == 'H':
        nim = input("Masukkan NIM yang akan dihapus: ")
        if nim in data_mahasiswa:
            del data_mahasiswa[nim]
            print("Data berhasil dihapus!")
        else:
            print("Tidak ada data yang ditemukan")

    elif pilih == 'C':
        nim = input("Masukkan NIM yang dicari: ")
        if nim in data_mahasiswa:
            mhs = data_mahasiswa[nim]
            print("\nData Mahasiswa:")
            print(f"NIM         : {nim}")
            print(f"Nama        : {mhs['nama']}")
            print(f"Tugas       : {mhs['tugas']}")
            print(f"UTS         : {mhs['uts']}")
            print(f"UAS         : {mhs['uas']}")
            print(f"Nilai Akhir : {mhs['nilai_akhir']:.1f}")
        else:
            print("Data yang input tidak ditemukan")

    elif pilih == 'K':
        print("Terima kasih telah menggunakan program ini.")
        break
