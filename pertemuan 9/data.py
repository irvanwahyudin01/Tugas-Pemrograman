nama=[]
nim=[]
NilaiT=[]
NilaiUts=[]
NilaiUas=[]
akhir=[]

data=1
addNA=input('Nama :')
addNI=int(input('Nim :'))
addT=int(input('Nilai Tugas :'))
addUT=int(input('Nilai UTS :'))
addUA=int(input('Nilai UAS :'))
hitung=(addT*0.30)+(addUT*0.35)+(addUA*0.35)

nama.append(addNA)
nim.append(addNI)
NilaiT.append(addT)
NilaiUts.append(addUT)
NilaiUas.append(addUA)
akhir.append(hitung)
u=(False,True)[input("apakah ingin memasukan data kembali? Y/n ") == "Y"]

while(u==True) :
    data+=1
    addNA=input('Nama :')
    addNI=int(input('Nim :'))
    addT=int(input('Nilai Tugas :'))
    addUT=int(input('Nilai UTS :'))
    addUA=int(input('Nilai UAS :'))
    hitung=int((addT*0.30)+(addUT*0.35)+(addUA*0.35))

    nama.append(addNA)
    nim.append(addNI)
    NilaiT.append(addT)
    NilaiUts.append(addUT)
    NilaiUas.append(addUA)
    akhir.append(hitung)
    u=(False,True)[input("apakah ingin memasukan data kembali? Y/n ") == "Y"]
i=0
no=1
print("========================================================================")
print(f"{('| No').ljust(5)}| {('Nama').ljust(20)}| {('Nim').ljust(10)}| {('Tugas').ljust(6)}| {('UTS').ljust(6)}| {('UAS').ljust(6)}| {('AKHIR').ljust(6)}|")
print("------------------------------------------------------------------------")
for i in range(data):
    print(f"{('| %d'%no).ljust(5)}| {(nama[i]).ljust(20)}| {str(nim[i]).ljust(10)}| {str(NilaiT[i]).ljust(6)}| {str(NilaiUts[i]).ljust(6)}| {str(NilaiUas[i]).ljust(6)}| {str('%d'%akhir[i]).ljust(6)}|",end="\n")
    i+=1
    no+=1
print("========================================================================")