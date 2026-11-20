# Meminta input nilai angka dari pengguna
nilai = float(input("Masukkan nilai: "))

# Menentukan Grade berdasarkan rentang nilai
if 85 <= nilai <= 100:
    grade = "A"
    print(f"Grade: {grade}")
elif 70 <= nilai <= 84:
    grade = "B"
    print(f"Grade: {grade}")
elif 55 <= nilai <= 69:
    grade = "C"
    print(f"Grade: {grade}")
elif 40 <= nilai <= 54:
    grade = "D"
    print(f"Grade: {grade}")
elif 0 <= nilai <= 39:
    grade = "E"
    print(f"Grade: {grade}")
else:
    print("Nilai tidak valid")