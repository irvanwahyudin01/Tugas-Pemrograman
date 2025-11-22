kontak = {
    "Ari": "081267889",
    "Dina": "085678990",
    "Budi": "082345678"
}


print("Kontak Ari:", kontak["Ari"])

a=input("Nama : ")
b=input("nomor: ")

kontak[a] = b
print("Setelah menambah Riko:", kontak)

print("ubah kontak dina : ")
c="088999776"
kontak["Dina"] = c
print("Setelah update Dina:", kontak)

print("Semua Nama:", list(kontak.keys()))

print("Semua Nomor:", list(kontak.values()))

print("Daftar kontak:")
for nama, nomor in kontak.items():
    print(nama, "|", nomor)

del kontak["Dina"]
print("Setelah hapus Dina:", kontak)