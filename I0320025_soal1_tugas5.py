# program untuk menyapa pengunjung hotel
print("=== Hotel del Luna ===")
print("Silahkan lengkapi data berikut terlebih dahulu: ")

# input data pengunjung hotel
nama = input('Masukkan nama Anda: ')
jenis_kelamin = input('Masukkan jenis kelamin Anda (L/P): ')

#output
if jenis_kelamin == 'L':
    print("Selamat datang, Tuan",nama + "!")
else:
    print("Selamat datang, Nyonya",nama + "!")


