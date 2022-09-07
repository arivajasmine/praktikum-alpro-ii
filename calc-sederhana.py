x = int(input("Masukkan bilangan pertama: "))
y = int(input("Masukkan bilangan kedua: "))
print('''
Pilih operasi kalkulator(1/2/3/4)
1. Tambah (+)
2. Kurang (-)
3. Kali (*)
4. Bagi (/)
''')
op = int(input("Masukkan pilihan: "))
if op == 1:
    print("Hasil:",x + y)
elif op == 2:
    print("Hasil:", x - y)
elif op == 3:
    print("Hasil:", x * y)
elif op == 4:
    print("Hasil:", x / y)
else:
    print("Operasi tidak ditemukan.")