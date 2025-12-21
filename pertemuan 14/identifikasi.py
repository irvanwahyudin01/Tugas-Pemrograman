nama = input("Masukkan nama lengkap: ")
telepon = input("Masukkan nomor telepon: ")
email = input("Masukkan email: ")

errors = []

if not nama.replace(" ", "").isalpha():
    errors.append("Nama lengkap harus hanya berisi huruf.")

if not telepon.isdigit():
    errors.append("Nomor telepon harus hanya berisi angka.")

if "@" not in email or "." not in email:
    errors.append("Email harus mengandung karakter '@' dan '.'")


if len(errors) == 0:
    print("\n Data pendaftaran valid.")
else:
    print("\n Terjadi kesalahan pada input:")
    for error in errors:
        print(error)
