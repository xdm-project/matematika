import os

def hitung_kecepatan():
    print("hitung kecepatan ready")
    jarak = float(input("masukan jarak: "))
    waktu = float(input("masukan waktu: "))
    kecepatan = jarak * waktu
    print("kecepatan: ", kecepatan, "\n" )


def luas_segitiga():
    print("hitung segitiga ready")
    alas = float(input("masukan alas: "))
    tinggi = float(input("masukan tinggi: "))
    luas = 0.5 * (alas * tinggi)
    print("luas segitiga: ", luas, "\n" )

def luas_balok():
    print("hitung luas balok")
    panjang = float(input("masukan panjang: "))
    lebar = float(input("masukan lebar: "))
    tinggi = float(input("masukan tinggi: "))
    luas = (2*panjang*lebar) + (2*panjang*tinggi) + (2*lebar*tinggi)
    print("luas balok : ", luas, "\n" )


def luas_bola():
    print("hitung bola ready")
    r = float(input(" jari-jari: "))
    luas = 4 * 3.14 * (r**2)
    print("luas bola : ", luas, "\n" )


while True:
    userinput = int(input("pilih rumus yang akan di pakai: \n\n1.hitung kecepatan\n\n2.luassegitiga\n\n3.luas balok\n\n4.luas bola\n\n0.keluar\n\npilih no berapa:"))
    os.system('clear')
    if(userinput == 1):
        hitung_kecepatan()
    elif(userinput == 2):
        luas_segitiga()
    elif(userinput == 3):
        luas_balok()
    elif(userinput == 4):
        luas_bola()
    else:
        break
