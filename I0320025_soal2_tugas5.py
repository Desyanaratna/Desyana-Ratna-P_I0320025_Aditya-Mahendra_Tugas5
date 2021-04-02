# program grading nilai
# input data dan nilai
nama = input("Masukkan nama: ")
nilai = int(input("Masukkan nilai: "))

#Output Nilai
if nilai >= 85:
    print("Halo,",nama + "!","Nilai anda setelah dikonversi adalah A")
    if nilai > 100:
        print("Nilai tidak Valid! Tidak dapat dikonversi!")
elif nilai >= 80:
    print("Halo,", nama + "!", "Nilai anda setelah dikonversi adalah A-")
elif nilai >= 75:
    print("Halo,", nama + "!", "Nilai anda setelah dikonversi adalah B+")
elif nilai >= 70:
    print("Halo,", nama + "!", "Nilai anda setelah dikonversi adalah B")
elif nilai >= 65:
    print("Halo,", nama + "!", "Nilai anda setelah dikonversi adalah C+")
elif nilai >= 60:
    print("Halo,", nama + "!", "Nilai anda setelah dikonversi adalah C")
elif nilai >= 0:
    print("Halo,", nama + "!", "Nilai anda setelah dikonversi adalah E")
else:
    print("Nilai tidak valid! Tidak dapat dikonversi!")