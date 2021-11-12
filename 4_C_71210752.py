#Soal No 4
#Menghitung jumlah suku ke-99 (Sn)
#Deret : 3,7,11,...

a = int(input("masukkan suku awal: "))
b = int(input("masukkan beda: "))
n = int(input("masukkan suku ke-n: "))

Sn = n/2 * (2 * a+(n-1) * b)

print("Jumlah suku ke-99: ", Sn)
