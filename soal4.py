# Meminta pengguna memasukkan tinggi segitiga n
n = int(input("Masukkan tinggi segitiga (n): "))

print("\n--- Segitiga Siku-Siku Normal ---")
for i in range(1, n + 1):
    print("*" * i)

print("\n--- Tantangan Tambahan: Versi Terbalik ---")
for i in range(n, 0, -1):
    print("*" * i)