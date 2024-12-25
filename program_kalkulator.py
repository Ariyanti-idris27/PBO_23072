# program_kalkulator
# mengimpor fungsi tertentu dari kalkulator dengan alias 'km'
 
import kalkulator_modul as km

# mengimpor fungsi tertentu dari kalkulator_modul 
from kalkulator_modul import tambah , kurang

# Mengimpor seluruh isi modul kalkulator dengan * (hindari di proyek besar)
from kalkulator_modul import *

print("===kalkulator sederhana===")
print("1. tambah ")
print("2. kurang")
print("3. kali")
print("4. bagi")
print("5. modulus")
print("6. pangkat")

# input pilihan operasi
pilihan = input ("pilih operasi(1-6):")

#input angka
angka1 = float(input("masukan angka pertama:"))
angka2 = float(input("masukan angka kedua:"))

#menggunakan alias 'km' untuk memanggil fungsi dari kalkulator_modul

if pilihan == '1':
    print("Hasil tambah:", km.tambah(angka1, angka2))
elif pilihan == '2':
    print("Hasil kurang:", km.kurang(angka1, angka2))
elif pilihan == '3':
    print("Hasil kali:", km.kali(angka1, angka2))
elif pilihan == '4':
    print("Hasil bagi:", km.bagi(angka1, angka2))
elif pilihan == '5':
    print("Hasil modulus:", km.modulus (angka1, angka2))  # Langsung menggunakan fungsi dari *import
elif pilihan == '6':
    print("Hasil pangkat:", km.pangkat (angka1, angka2))  # Langsung menggunakan fungsi dari *import
else:
    print("Pilihan tidak valid!")


