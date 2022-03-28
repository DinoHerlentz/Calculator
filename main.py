def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    return x / y

def modulus(x, y):
    return x % y

def div(x, y):
    return x // y

print("\bPilih salah satu :\b\n1. Penjumlahan.\n2. Pengurangan.\n3. Perkalian.\n4. Pembagian.\n5. Eksponen.\n6. Modulus.\n7. Floor Division\n")

while True:
    choice = input("Masukkan pilihan anda (1/2/3/4/5/6) : ")
    
    if choice in ("1", "2", "3", "4", "5", "6"):
        try:
            num1 = float(input("Masukkan angka pertama : "))
            num2 = float(input("Masukkan angka kedua : "))
        except ValueError:
            print("Mohon masukkan hanya angka!")
            break
        
        if choice == "1":
            print("Hasil dari {} + {} = {}".format(num1, num2, tambah(num1, num2)))
        elif choice == "2":
            print("Hasil dari {} - {} = {}".format(num1, num2, kurang(num1, num2)))
        elif choice == "3":
            print("Hasil dari {} x {} = {}".format(num1, num2, kali(num1, num2)))
        elif choice == "4":
            print("Hasil dari {} : {} = {}".format(num1, num2, bagi(num1, num2)))
        elif choice == "5":
            print("Hasil dari {} % {} = {}".format(num1, num2, modulus(num1, num2)))
        elif choice == "6":
            print("Hasil dari {} // {} = {}".format(num1, num2, div(num1, num2)))
        
        lanjut = input("Apakah anda masih ingin menggunakan kalkulator? (ya/tidak) : ")
        
        if lanjut == "tidak":
            break
        elif lanjut != "ya":
            print("Masukkan anda tidak valid!")
    else:
        print("Masukkan anda tidak valid!")
