# Meminta batas bawah dan batas atas dari pengguna
batas_bawah = int(input("Batas bawah: "))
batas_atas = int(input("Batas atas: "))

bilangan_prima = []

for num in range(batas_bawah, batas_atas + 1):
    if num > 1:
        # Perulangan untuk memeriksa pembagi
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            bilangan_prima.append(str(num))

# Menampilkan hasil sesuai format contoh
print(f"Bilangan prima: {' '.join(bilangan_prima)}")
print(f"Jumlah: {len(bilangan_prima)}")