class Mahasiswa():
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm
        
    def penghitung_kata(self):
        jumlah_kata = len(nama)
        self.nama = self.nama.split(' ')
        
        if len(nama)% 2 == 0:
            print (nama,",",jumlah_kata, "huruf", "," ,"Genap")
        else:
            print (nama,",",jumlah_kata, "huruf", "," ,"Ganjil")
            
    def last_digit(self):
        angka = (npm%10)
        if (npm% 2) == 0:
            print (npm,",","angka terakhir {}".format(angka),"," ,"Genap")
        else:
            print (npm,",","angka terakhir {}".format(angka),"," ,"Ganjil")
        
nama = input("Input Nama : ")   
npm = int(input("Input NPM: "))      
a = Mahasiswa(nama, npm)
a.penghitung_kata()
a.last_digit()
