import random

batas_maks = input ("Masukkan batas maksimal angka yang ingin anda tebak. ")
                  
if batas_maks.isdigit() :
    batas_maks = int (batas_maks)

    if batas_maks <= 1:
        print ("Masukkan angka yang lebih dari angka 1 lain kali. ")
        quit()
else : 
    print("Masukkan angka lain kali. ")
    quit()
    
angka_acak = random.randint(0, batas_maks)
jumlah_tebakan = 0

while True:
    jumlah_tebakan += 1
    tebak = input ("Buatlah tebakan angka anda. ")

    if tebak.isdigit() :
        tebak = int (tebak)

    else : 
        print("Masukkan angka lain kali. ")
        continue

    if tebak == angka_acak :
        print ("Anda berhasil menebaknya. Selamat! ")
        break

    elif tebak > angka_acak : 
        print ("Angka yang anda tebak berada di atas. Masukkan nilai angka lebih rendah. ")

    else : 
        print ("Angka yang anda tebak berada di bawah. Masukkan angka lebih tinggi. ")

print ("Anda menebak angka", tebak, "dalam jumlah", jumlah_tebakan, "tebakan. ")
