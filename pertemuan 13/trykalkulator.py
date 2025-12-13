try:
    a = int(input("Inputkan bilangan pertama  : "))
    b = int(input("Inputkan bilangan kedua    : "))
except ValueError:
    print("Error: Input harus berupa angka!")
    exit()

print("List Operasi")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")
print("===========================")

c = input("Pilih operasi yang akan dilakukan : ")

try:
    if c == "1":
        h = a + b
    elif c == "2":
        h = a - b
    elif c == "3":
        h = a * b
    elif c == "4":
        h = a / b
    else:
        raise Exception("Error: Operator tidak valid!")
except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan nol!")
    exit()
except Exception as e:
    print(e)
    exit()

print("Hasil dari operasi adalah :", h)
