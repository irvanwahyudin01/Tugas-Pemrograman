A= [1,2,7,2,4]


#list akses
print(A[2])
print(A[1:4])
print(A[4])

#ubah element
A[3]="iya"
print(A[3])

A[3:]=[2,3,2]
print(A[3:])

#tambah elemen
B= A[0:2]
print(B[:])

B.extend(["stringini"])
print(B[:])

B.extend([5,3,2])
print(B[:])

print(A[:]+B[:])