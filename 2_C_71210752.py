#Soal No 2 Test Case 1
#Penghitung kata yang muncul dari sebuah kalimat

string = input("Masukkan kalimat: ")
substring = input("Masukkan kata untuk dihitung: ")
count = string.count(substring)
print('ada', count, 'buah kata', substring)

#Soal No 2 Test Case 2
#Penghitung kata yang muncul dari sebuah kalimat

string = input("Masukkan kalimat: ")
substring = input("Masukkan kata untuk dihitung: ")
count = string.casefold().count(substring)
print('ada', count, 'buah kata', substring)
