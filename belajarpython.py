a = 5
b = 6
c= a + b 

print("nilai c = ",c)

def tambahData(a, b):
    return a + b


if(a > b ):
    print("NILAI a LEBIH BESAR DAI b")p
else:
    print("NILAI b LEBIH BESAR DAI a")

nilai_mahasiswa = [80, 75, 84, 90]

#print(range(len(nilai_mahasiswa)))

#print(range(5))

for i in range(len(nilai_mahasiswa)): 
    print("NILAI MAHASISWA KE-", i, "ADALAH", nilai_mahasiswa[i])

####

def rata_Nilai(nilai_a):
    jumlah = 0
    for i in range(len(nilai_a)):
        jumlah += nilai_a[i]
    return jumlah / len(nilai_a)

print("RATA-RATA NILAI MAHASISWA ADALAH", rata_Nilai(nilai_mahasiswa))