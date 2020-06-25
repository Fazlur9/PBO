def Terbilang(bil):
    angka=["","Satu","Dua","Tiga","Empat","Lima","Enam","Tujuh","Delapan","Sembilan","Sepuluh","Sebelas"]
    Hasil =" "
    n = int(bil)
    if n >= 0 and n <= 11:
        Hasil = Hasil + angka[n]
    elif n < 20:
        Hasil = Terbilang(n % 10) + " Belas"
    elif n < 100:
        Hasil = Terbilang(n / 10) + " Puluh" + Terbilang(n % 10)
    elif n < 200:
        Hasil = " Seratus" + Terbilang(n - 100)
    elif n < 1000:
        Hasil = Terbilang(n / 100) + " Ratus" + Terbilang(n % 100)
    elif n == 1000 :
        Hasil = " Seribu"
    else:
        Hasil="Angka hanya sampai seribu"
    return Hasil

if __name__ == '__main__':
    bil = input("Input Angka : ")
    blng= Terbilang(bil )
    print (bil+blng)