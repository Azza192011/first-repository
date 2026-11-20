# Meminta input n
n = int(input("Masukkan bilangan bulat positif n: "))

if n > 0:
    bilangan_list = []
    jumlah_total = 0
    jumlah_genap = 0

    for i in range(1, n + 1):
        bilangan_list.append(str(i))
        jumlah_total += i
        if i % 2 == 0:
            jumlah_genap += i

    print(f"Deret bilangan: {', '.join(bilangan_list)}")
    print(f"Jumlah seluruh bilangan: {jumlah_total}")
    print(f"Jumlah bilangan genap saja: {jumlah_genap}")
else:
    print("Harap masukkan bilangan bulat positif!")