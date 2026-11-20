# Meminta input bilangan bulat dari pengguna
angka = int(input("Masukkan bilangan: "))

# Mengecek apakah bilangan positif, negatif, atau nol
if angka > 0:
    sifat_bilangan = "positif"
elif angka < 0:
    sifat_bilangan = "negatif"
else:
    sifat_bilangan = "nol"

# Mengecek ganjil/genap jika bilangan bukan nol
if angka != 0:
    if angka % 2 == 0:
        jenis_bilangan = "genap"
    else:
        jenis_bilangan = "ganjil"
    print(f"Bilangan {sifat_bilangan} dan {jenis_bilangan}")
else:
    print("Bilangan nol")