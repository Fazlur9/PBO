class Pertemuan3():
    def pertemuan3_latihan1(self):
        a=1
        b=2

        z = a + b
        print ("a+b =",z)

        z = a - b
        print ("a-b  =",z)

        z = a * b
        print ("a*b =",z)

        z = a / b
        print ("a/b  =",z)

        z = a % b
        print ("sisa bagi =",z)

        z = a ** b
        print ("a**b =",z)
    
    def pertemuan3_latihan2(self):
        a=int(input("masukan nilai A = "))

        a += 3
        print(a)

        a -= 3
        print(a)

        a /= 3
        print(a)

        a *= 3
        print(a)

        a **= 3
        print(a)

        a %= 3
        print(a)    
    
    def pertemuan3_latihan3(self):
        a= True
        b= False

        c= a and b 
        print("jika A={} and B={} = {}". format(a,b,c))

        c= a or b 
        print("jika A={} or B={} = {}". format(a,b,c))

        c= not a 
        print("jika A={} maka not A = {}". format(a,b,c))    
    
    def pertemuan3_latihan4(self):
        a=int(input("Masukan Nilai A = "))
        b=int(input("Masukan Nilai B = "))

        c= a & b 
        print("{} & {} = {}". format(a,b,c))

        c= a | b 
        print("{} | {} = {}". format(a,b,c))

        c= a ^ b 
        print("{} ^ {} = {}". format(a,b,c))

        c= ~a  
        print("~{} = {}". format(a,b,c))

        c= a << b 
        print("{} << {} = {}". format(a,b,c))

        c= a >> b 
        print("{} >> {} = {}". format(a,b,c))
    
    def pertemuan3_latihan5(self):
        a= input("lanjut (y/t)?")
        if a in ["y", "Y"]:
            print("baiklah")
        else:
            print("okelah. . .")    
    
    def pertemuan3_latihan6(self):
        a= input("lanjut (y/t)?")
        if a in ["y", "Y"]:
            print("baiklah")
        elif a in ["t", "T"]:
            print("okelah. . .")
        else:
            print("maaf keywordnya yang harus anda input Y/T")    
    
    def pertemuan3_tugas1(self):
        #fungsi dari int yaitu mengkonfersi bilangan maupun string angka menjadi bilangan bulat(integer).
        #fungsi input yaitu untuk menerima baris input(masukan) dari user dan mengembalikannya dalam bentuk string.
        a=int(input("Masukan Nilai a = "))
        b=int(input("Masukan Nilai b = "))

        z = a + b
        print ("a+b =",z)

        z = a - b
        print ("a-b  =",z)

        z = a * b
        print ("a*b =",z)

        z = a / b
        print ("a/b  =",z)

        z = a % b
        print ("sisa bagi =",z)

        z = a ** b
        print ("a**b =",z)

    def pertemuan3_tugas2(self):
        #1. Fungsi-fungsi operator bitwise
        #&  = operasi bitwise "and" ini akan memproses bit per bit dari kedua variabel, jika kedua bit sama-sama 1, maka hasilnya juga 1, selain kondisi tersebut,nilai akhirnya adalah 0
        #|  = hasilnya akan bernilai 0 jika kedua bit bernilai 0, selain itu nilai bit akan di set menjadi 1
        #^  = hasilnya akan bernilai 1 jika salah satu dari kedua variabel bernilai 1 (namun tidak keduanya). atau dengan kata lain jika kedua bit berlainan, hasilnya 1 tapi kalau sama-sama 0 atau sama-sama 1, hasilnya 0.
        #~  = operasi not yang akan membalikan nilai bit sebuah variabel dari 0 menjadi 1, dan 1 menjadi 0. namun perhitungan bit ini sedikit membinggungkan karena jika kita membalikan seluruh bit saja, hasilnya tidak sesuai dengan apa yang dihitung python.
        #     ini berkaitan dengan cara bahasa python menyimpan angka biner. angka biner di dalam bahasa python disimpan dalam format "two complement". secara singkat, rumusnya adalah "-x - 1", sehingga ~x = -10 - 1 = 11 (desimal).
        #<< = operator shift left dimana nilai dari sebuah variabel akan digeser sebanyak 1 digit ke kiri. ketika hasil pergeseran ke kiri, digit paling kanan akan diisi angka 0. setiap pergeseran 1 tempat ke kiri akan mengkali 2 nilai asal.
        #>> = operator shift right dimana bahasa python akan menggeser posisi bit dalam sebuah variabel ke kanan sebanyak 1 tempat. hasilnya akan menggeser nilai variabel ke arah kanan, sehingga digit paling kanan akan dihapus.

        #2. contoh kasus operator tenary

        a=int(input("Masukan Nilai a = "))
        b=int(input("Masukan Nilai b = "))

        if a != b:
            if a > b:
                print ("a lebih besar dari b")
            else:
                print("b lebih besar dari a")
        else:
            print("nilai a dan b sama besar")    
 
class Pertemuan4():
    def pertemuan4_latihan1(self):
        list1_int=[1,2,3,4,5,6]
        list_string=['info 1', 'info 2', 'info 3']
        list_string=["PBO", "pemrograman web", "Grafika Komputer"]
    
    def pertemuan4_latihan2(self):
        nilai_matakuliah=[70, 80, 90, 90, 13]
        rata_rata= (sum(nilai_matakuliah)/len(nilai_matakuliah))
        print("Nilai Matakuliah = ", nilai_matakuliah)
        print("Nilai Rata-rata = ", rata_rata)    

    def pertemuan4_latihan3(self):
        tuple_string= ("HTML", "CSS", "Python")
        tuple_int= (1,2,3,4,5)
        tuple_pub= "a", "b", "c"

        print("tuple sting: ", tuple_string)
        print("tuple int: ", tuple_int)
        print("tuple pub: ", tuple_pub)    

    def pertemuan4_latihan4(self):
        nilai_mk1={10, 20, 30, 40, 50, 60}
        nilai_mk2={40, 50, 10}

        print(nilai_mk1.intersection(nilai_mk2))
        print(nilai_mk1.union(nilai_mk2))    
    
    def pertemuan4_tugas2(self):
        #Pengerian
        #Dictionary merupakan tipe data yang anggotanya terdiri dari pasangan kunci:nilai (key:value).
        #Dictionary bersifat tidak berurut(unordered) sehingga anggotanya tidak memiliki indeks.

        #Membuat Dictionary
        #Dictionary dibuat dengan menempatkan anggotanya di dalam tanda kurung kurawal {}, dipisahkan dengan tanda koma.
        #Anggota Dictionary terdiri dari pasangan kunci:nilai. kunci harus bersifat unik, tidak boleh ada dua kunci yang sama dalam dictionary.

        #membuat Dictionary kosong
        dict_0 = {}

        #dictionary dengan kunci integer
        dict_1 = {1 : 'baju', 2: 'celana'}
        print(dict_1)
        print(dict_1[1])
        print(dict_1[2])

        #dictionary dengan kunci campuran
        dict_2 = {'warna': 'hijau', 1: [2,3,4]}
        print(dict_2)
        print(dict_2['warna'])
        print(dict_2[1])
        print("----------------------------------")
        #Mengakses Anggota Dictionary
        #Dictionary tidak menggunakan indeks. Anggota dictionary diakses den' menggunakan kuncinya. selain itu, bisa juga diakses
        #dengan menggunakan fungsi get().
        #Dengan menggunakan fungsi get() bila kunci tidak ada di dalam dictionary, maka akan dikembalikan None. bila tidak 
        #menggunakan fungsi get(), maka akan terjadi error "KeyError"  bila kunci yang hendak diakses tidak ada di dalam dictionary.
        #contoh

        cth1_dict = {'nama': 'Koko', 'usia': 25}
        print(cth1_dict['nama'])
        #menggunakan fungsi get()
        print(cth1_dict.get('usia'))
        #mengakses kunci yg tidak tersedia dikembalikan  None
        print(cth1_dict.get('asal'))
        print("----------------------------------")

        #Menggubah Anggota Dictionary
        #Dictionary bersifat mutabel. kita bisa menambahkan atau mengubah nilai dari anggotanya menggunakan operator penugasan.
        #bila kunci sudah ada, maka akan di update nilainya, jika belum, maka akan di tambahkan sebagai kunci baru.
        #contoh
        cth2_dict = {'nama': 'Koko', 'usia': 25}

        cth2_dict['usia'] = 26 #update nilai
        print(cth2_dict)

        cth2_dict['alamat'] = 'Ternate' #menambah anggota
        print(cth2_dict)
        print("----------------------------------")

        #Menghapus Anggota Dictionary
        #Kita bisa menghapus anggota tertentu pada dictionary dengan menggunakan fungsi pop(). 
        #Fungsi ini menghapus anggota dengan mengembalikan kunci dari anggota tersebut.
        #Fungsi lain, popitem() digunakan untuk menghapus anggota acak dari dictionary. Untuk menghapus semua anggota dictionary, 
        #bisa menggunakan fungsi clear().
        #Selain itu kita juga bisa menggunakan kata kunci del untuk menghapus anggota tertentu atau menghapus dictionary itu sendiri.
        #contoh

        # membuat dictionary baru 
        pangkat = {1:1, 2:4, 3:9, 4:16, 5:25} 

        # menghapus anggota tertentu 
        # output: 9 
        print(pangkat.pop(3)) 

        # menghapus anggota secara acak 
        # output: (5, 25)
        print(pangkat.popitem()) 

        # yang tersisa adalah {1: 1, 2: 4, 4: 16} 
        print(pangkat) 

        # delete 5 
        del pangkat[4] 

        # output: {1: 1, 2: 4} 
        print(pangkat) 

        # menghapus semua anggota 
        pangkat.clear() 

        # menghapus dictionary pangkat 
        del pangkat 

class Pertemuan5():
    def pertemuan5_latihan1(self):
        my_variabel = "hai hamtaro"
        for variabel_baru in my_variabel:
            print("for string:", variabel_baru)
            
        my_list = ["aku", "kamu", "dia"]
        my_tuple = (1,5,6,7)
        for variabel_baru3 in my_tuple:
            print("for list or tuple", variabel_baru3)    
    
    def pertemuan5_latihan2(self):
        a=["sabun", "gula", "kopi"]
        b=["sagu", "nasi", "lauk"]
        gabungan=[a,b]
        for belanja in gabungan:
            print(belanja)
            for belanja_detail in belanja:
                print("belanja_detail")    
    
    def pertemuan5_latihan3(self):
        for variabel_baru4 in range(10):
           print("for range", variabel_baru4)

        for variabel_baru5 in range(1,10,2):
                print("for terstruktur", variabel_baru5)
    
    def pertemuan5_latihan4(self):
        nama_makanan=["nasi", "sayur", "sambal"]
        for pilihan_makanan in nama_makanan:
            print("pilihan makanan:", pilihan_makanan)
            if pilihan_makanan == "sayur":
                print("ini makanan diet")
                break
                print("Selamat Diet!!")
        else:
            print("anda telah keluar dari loop")
            print("yah kasiang")    
    
    def pertemuan5_latihan5(self):
        nama_makanan=["nasi", "sayur", "sambal"]
        for pilihan_makanan in nama_makanan:
            print("pilihan makanan:", pilihan_makanan)
            if pilihan_makanan == "sayur":
                print("ini makanan diet")
                continue
                #pass(tidak di cetak)
                print("Selamat Diet!!")
        else:
            print("anda telah keluar dari loop")
            print("yah kasiang")    
    
    def pertemuan5_latihan6(self):
        while True:
            a_username=input("Masukan Username:")
            a_password=input("Masukan Password:")
            
            if a_username == "admin" and a_password == "ternate":
                print("Selamat anda berhasil login :)")
                break
            else:
                print("username & password tidak sesuai, silahkan kembali login")    
  
    def pertemuan5_latihan7(self):
        status = False
        batas = 3
        tabel_username = ["admin", "sayaadmin", "sayajugaadmin"]
        tabel_password = ['ummu', 'ternate', 'akademik']
        while batas > 0:
            tanya_username = input("Masukan Username Anda: ")
            tanya_password = input("Masukan Password Anda: ")
            for password in tabel_password:
                for a_username in tabel_username:
                    if tanya_password == password and tanya_username == a_username:
                        print("Selamat Anda berhasil Login")
                        status = True
                        break
            if not status:
                print("Password & Username yang anda masukan salah, silahkan kembali login")
                batas = batas - 1
                continue
            else:
                break    
    
    def pertemuan5_tugas1(self):
        def tambah(x, y):
            return x + y

        def kurang(x, y):
            return x - y

        def kali(x, y):
            return x * y

        def bagi(x, y):
            return x / y


        while True:
            print('\nMenu operasi:\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Tutup')
            operasi = int(input('silahkan masukan operasi pilihan (dalam angka): '))
            if operasi == 1:
                x = int(input('masukan angka pertama: '))
                y = int(input('masukan angka ke dua: '))
                print('Hasilnya: {}'.format(tambah(x, y)))
            elif operasi == 2:
                x = int(input('masukan angka pertama: '))
                y = int(input('masukan angka ke dua: '))
                print('Hasilnya: {}'.format(kurang(x, y)))
            elif operasi == 3:
                x = int(input('masukan angka pertama: '))
                y = int(input('masukan angka ke dua: '))
                print('Hasilnya: {}'.format(kali(x, y)))
            elif operasi == 4:
                x = int(input('masukan angka pertama: '))
                y = int(input('masukan angka ke dua: '))
                print('Hasilnya: {}'.format(bagi(x, y)))
            elif operasi == 5:
                break
            else:
                print('Operasi tidak dikenali')    

class Pertemuan6():
    def pertemuan6_latihan1(self):
        def helloworld():
            print("ini adalah fungsi menampilkan helloworld")
        helloworld()    
    
    def pertemuan6_latihan2(self):
        def tambah(x,y):
            a=x+y
            print(a)
        tambah(5,6)    
    
    def pertemuan6_latihan3(self):
        def hello(nama):
            print(f"hello {nama}")
        hello("zul")    
    
    def pertemuan6_latihan4(self):
        def input_barang(nama,harga):
            print("Nama Barang: ", nama)
            print("Harga Barang: ", harga)
        a=input("masukan nama barang:")
        b=input("masukan harga barang:")
        input_barang(a,b)    
    
    def pertemuan6_latihan5(self):
        def hitung():
            umur=int(input("masukan umur kamu: "))
            jj=umur * 369 * 24 * 60 * 60
            print(f"kamu sudah hidup selama {jj}.detik")
        print("Selamat datang di program hitung detik umur")
        hitung()    
    
    def pertemuan6_latihan6(self):
        def hitung_gaji():
            nama=(input("Masukan Nama Anda:"))
            gol=(input("masukan golongan:"))
            if gol == "1":
                gaji=1000000
                tunjangan=250000
                total=gaji+tunjangan
                print(f"Total gaji yang anda terima {total}")
            elif gol == "2":
                gaji=2000000
                tunjangan=500000
                total=gaji+tunjangan
                print(f"Total gaji yang anda terima {total}")
            elif gol == "3":
                gaji=3000000
                tunjangan=700000
                total=gaji+tunjangan
                print(f"Total gaji yang anda terima {total}")
            else:
                print("mohon masukan golongan anda")
        print("Selamat Datang di Program Hitung Gaji")
        print("--------------------------")
        devisi=input("masukan devisi anda:")
        if devisi == "kantor":
            hitung_gaji()
        elif devisi == "lapangan":
            hitung_gaji()
            transportasi=100000
            print("tambahkan tunjangan lapangan", transportasi)
        else:
            print("devisi yang anda masukan salah")    
    
    def pertemuan6_tugas1(self):
        #1. penjelasan constructor dan destructor
        #constructor merupakan metode spesial yang dieksekusi saat kita membuat sebuah objek kelas
        #constructor didefinisikan mengunakan __init__()
        class Car:
            def __init__(self):
                print("Hello World")
                print("--------------------")
        car = Car()

        #destructor dijalankan ketika objek di hancurkan(destroy)
        #destructor bisa sangat berguna dalam melenggangkan resources sebelum keluar dari program seperti menutup file, mengosongkan memori, dll
        #destructor didefinisikan mengunakan __del__()

        class Vehicle:
            def __init__(self):
                print('vehicle created')
            def __del__(self):
                print('memanggil destructor, vechicle deleted.')
                print("--------------------")
        car = Vehicle()
        print("Hello World")
        print("--------------------")

        #2. Studi Kasus

        from datetime import datetime, date

        print("Your date of birth (dd mm yyyy)")
        date_of_birth = datetime.strptime(input("--->"), "%d %m %Y")

        def calculate_age(born):
            today = date.today()
            return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

        age = calculate_age(date_of_birth)

        print(age)
        print("--------------------")    

class Pertemuan7():
    def pertemuan7_latihan1(self):
        class Mahasiswa:
            def __init__(self):
                self.nama = "Fazlur"
                self.nilai = (90,70,90,80)
            def hitung_nilai(self):
                return sum(self.nilai)/len(self.nilai)
        mahasiswa = Mahasiswa()
        print("Nama :", mahasiswa.nama)
        print("Total Nilai :", mahasiswa.hitung_nilai())    
    
    def pertemuan7_latihan2(self):
        class Mahasiswa:
            def __init__(self, nama, nilai):
                self.nama = nama
                self.nilai = nilai
            def hitung_nilai(self):
                return sum(self.nilai)/len(self.nilai)
        mahasiswa = Mahasiswa("Fazlur", (90,70,70,70))
        print("Nama :", mahasiswa.nama)
        print("Total Nilai :", mahasiswa.hitung_nilai())    
    
    def pertemuan7_latihan3(self):
        class Mahasiswa:
            def __init__(self, nama, kelas):
                self.nama = nama
                self.kelas = kelas
            def __str__(self):
                return f"nama {self.nama}, kelas: {self.kelas}"
            def __repr__(self):
                return f"<nama ('{self.nama}', kelas: {self.kelas})>"
        c = Mahasiswa("yuyun",45)
        print(c)    
    
    def pertemuan7_tugas1(self):
        print("__str__()")
        print("Metode ini mengembalikan representasi string dari objek.")     
        print("Metode ini disebut ketika fungsi print () atau str () dipanggil pada suatu objek.") 

        print("__repr__()")
        print("Metode ini harus mengembalikan objek String. Jika kita tidak mengimplementasikan fungsi __str __ () untuk sebuah kelas,")  
        print("maka implementasi objek bawaan digunakan yang sebenarnya memanggil fungsi __repr __ ().") 
        print("Fungsi __repr __ () mengembalikan representasi objek. Itu bisa berupa ekspresi python yang valid seperti tuple, kamus, string dll.") 
        print(" Metode ini dipanggil ketika fungsi repr () dipanggil pada objek, ")
        print("dalam hal ini, fungsi (__repr __ ()) harus mengembalikan sebuah String jika tidak kesalahan akan dilempar.") 

class Pertemuan8():
    def pertemuan8_latihan1(self): 
        class Mahasiswa:
            nama= ""
            __kelas= ""
            jurusan= ""
            def __init__(self, nama, kelas, jurusan):
                self.nama = nama
                self.__kelas = kelas
                self.jurusan = jurusan
            def tampil(self):
                print("Nama : ", self.nama)
                print("Kelas : ", self.__kelas)
                print("Jurusan : ", self.jurusan)

        siswa1 = Mahasiswa("Fazlur", "Info 5", "Sistem Informasi")
        siswa1.tampil()
        '''print("kelas : ", siswa1.kelas) #error karena mencoba mengakses dari luar'''
    
class Pertemuan9():
    def pertemuan9_latihan1(self):
        class Mahasiswa:
            nama= ""
            __kelas= ""
            jurusan= ""
            def __init__(self, nama, kelas, jurusan):
                self.nama = nama
                self.__kelas = kelas
                self.jurusan = jurusan
            def tampil(self):
                print("Nama : ", self.nama)
                print("Kelas : ", self.__kelas)
                print("Jurusan : ", self.jurusan)
                print("============================")
                
        class Krs(Mahasiswa):
            def __init__(self, nama, kelas, jurusan, semester):
                super(). __init__(nama, kelas, jurusan)
                self.semester = semester
            def matakuliah(self):
                matakuliah=[]
                tanya = input("apakah anda ingin menginput matakuliah ya|tidak?")
                if tanya == "ya":
                    a = input("silahkan masukan matakuliah : ")
                    matakuliah.append(a)
                    print("Matakuliah Berhasil di tambahkan!")
                    print("matakuliah yang di ambil :", matakuliah)
                else:
                    print("anda tidak menginput matakuliah")

        siswa1 = Mahasiswa("Nina", "3", "Sistem Informasi")
        siswa2 = Krs("Kartika", "3", "Jaringan", "Semester 4")

        print("Tampil Data Siswa I",)
        siswa1.tampil()
        print("Tampil Data Siswa II",)
        siswa2.tampil()

        #atribut baru pada class krs : semester
        print("Semester : ", siswa2.semester)
        siswa2.matakuliah()
        
    def pertemuan9_tugas1(self):  
        class Polygon:
            def __init__(self, no_of_sides):
                self.__n = no_of_sides
                self.sides = [0 for i in range(no_of_sides)]

            def inputSides(self):
                self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.__n)]

            def dispSides(self):
                for i in range(self.__n):
                    print("Side",i+1,"is",self.sides[i])

        class Triangle(Polygon):
            def __init__(self):
                Polygon.__init__(self,3)

            def findArea(self):
                a, b, c = self.sides
                # calculate the semi-perimeter
                s = (a + b + c) / 2
                area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
                print('The area of the triangle is %0.2f' %area)

        t = Triangle()
        t.inputSides()
        t.dispSides()
        t.findArea()
 
class Pertemuan10():
    def pertemuan10_latihan1(self):
        class Burung:
            def __init__(self, name, age):
                self.name = name
                self.age = age
            
            def info(self):
                print(f"saya seekor burung bernama {self.name}. dan berumur {self.age}")
            
            def gerak_cepat(self):
                print("Terbang")

        class Singa:
            def __init__(self, name, age):
                self.name = name
                self.age = age
            
            def info(self):
                print(f"saya seekor singa bernama {self.name}. dan berumur {self.age}")
            
            def gerak_cepat(self):
                print("Berlari")

        burung1 = Burung("Leo", 2.5)
        singa1 = Singa("Sipu", 4)

        for animal in (burung1, singa1):
            animal.gerak_cepat()
            animal.info()
            animal.gerak_cepat()    
    
    def pertemuan10_tugas1(self):
        #1 method overloading dan overriding
        #Dalam Python, Anda dapat mendefinisikan metode sedemikian rupa sehingga ada beberapa cara untuk menyebutnya.

        #Diberikan metode atau fungsi tunggal, kita dapat menentukan jumlah parameter sendiri.

        #Bergantung pada definisi fungsi, dapat dipanggil dengan parameter nol, satu, dua atau lebih.

        #Ini dikenal sebagai metode overloading. Tidak semua bahasa pemrograman mendukung metode overloading, tetapi Python dapat melakukannya.
        # Contoh
        class Human:

            def sayHello(self, name=None):
            
                if name is not None:
                    print('Hello ' + name)
                else:
                    print('Hello ')
                print("======================")

        # Create instance
        obj = Human()
            
        # Call the method
        #obj.sayHello()
            
        # Call the method with a parameter
        obj.sayHello('Guido')


        #Overriding adalah properti dari kelas untuk mengubah implementasi metode yang disediakan oleh salah satu kelas dasarnya.
        #Dalam metode Python overriding terjadi hanya dengan mendefinisikan di kelas anak metode dengan nama metode yang sama di kelas induk. 
        #Ketika Anda mendefinisikan metode dalam objek Anda membuat yang terakhir ini mampu memenuhi panggilan metode itu, sehingga implementasi dari leluhurnya tidak ikut berperan.
        # Contoh
        # Defining parent class 
        class Parent(): 
              
            # Constructor 
            def __init__(self): 
                self.value = "Inside Parent"
                  
            # Parent's show method 
            def show(self): 
                print(self.value) 
                  
        # Defining child class 
        class Child(Parent): 
              
            # Constructor 
            def __init__(self): 
                self.value = "Inside Child"
                  
            # Child's show method 
            def show(self): 
                print(self.value) 
                print("======================")  
                  
        # Driver's code 
        obj1 = Parent() 
        obj2 = Child() 
          
        obj1.show() 
        obj2.show() 

        # 2. Studi kasus
        from math import pi


        class Shape:
            def __init__(self, name):
                self.name = name

            def area(self):
                pass

            def fact(self):
                return "I am a two-dimensional shape."

            def __str__(self):
                return self.name


        class Square(Shape):
            def __init__(self, length):
                super().__init__("Square")
                self._length = length

            def area(self):
                return self._length**2

            def fact(self):
                return "Squares have each angle equal to 90 degrees."


        class Circle(Shape):
            def __init__(self, radius):
                super().__init__("Circle")
                self._radius = radius

            def area(self):
                return pi*self._radius**2


        a = Square(4)
        b = Circle(7)
        print(b)
        print(b.fact())
        print(a.fact())
        print(b.area())    
    
class Pertemuan11():
    def pertemuan11_latihan1(self):
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
     
class Pertemuan12():
    def pertemuan12_latihan1(self):
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
    
class Pertemuan13():
    def pertemuan13_latihan1(self):
        daftar_input = input('Input Nilai, pisahkan dengan tanda koma. (contoh: Absen,Tugas,UTS,UAS) : ')
        list_angka = daftar_input.split(',')
        daftar_baru = [int(x) for x in list_angka]
         
        jumlah = 0
        for angka in daftar_baru:
            jumlah += angka
        rata_rata = jumlah / len(daftar_baru)

        if rata_rata >= 80 :
            print('Nilai rata-rata: {},'.format(rata_rata), "A")
        elif rata_rata >= 70 :
            print('Nilai rata-rata: {},'.format(rata_rata), "B")
        elif rata_rata >= 55 :
            print('Nilai rata-rata: {},'.format(rata_rata), "C")
        elif rata_rata >= 40 :
            print('Nilai rata-rata: {},'.format(rata_rata), "D")
        elif rata_rata <= 39 :
            print('Nilai rata-rata: {},'.format(rata_rata), "E")

   
class Menu():
    def pilih_pertemuan(self):
        while True:
            print('\nPertemuan:\n1. Operator\n2. List,Tuple,Set\n3. Pengulangan\n4. Function\n5. Class\n6. Encapsulation\n7. Inheritance\n8. Polymorphism\n9. Hitung Huruf\n10. Angka Terbilang\n11. Hitung Nilai\n12. Tutup')
            operasi = int(input('silahkan masukan pilihan (dalam angka): '))
            if operasi == 1:
                print('\nLatihan/Tugas:\n1. Aritmatika\n2. Penugasan\n3. Logika\n4. Bitwise\n5. Tenary 1\n6. Tenary 2\n7. Tugas 1\n8. Tugas 2\n9. Kembali')
                pilih = int(input('silahkan masukan pilihan (dalam angka): '))
                if pilih == 1:
                    p3 = Pertemuan3()
                    p3.pertemuan3_latihan1()
                elif pilih == 2:
                    p3 = Pertemuan3()
                    p3.pertemuan3_latihan2()
                elif pilih == 3:
                    p3 = Pertemuan3()
                    p3.pertemuan3_latihan3()
                elif pilih == 4:
                    p3 = Pertemuan3()
                    p3.pertemuan3_latihan4()
                elif pilih == 5:
                    p3 = Pertemuan3()
                    p3.pertemuan3_latihan5()
                elif pilih == 6:
                    p3 = Pertemuan3()
                    p3.pertemuan3_latihan6()
                elif pilih == 7:
                    p3 = Pertemuan3()
                    p3.pertemuan3_tugas1()
                elif pilih == 8:
                    p3 = Pertemuan3()
                    p3.pertemuan3_tugas2()
                elif pilih == 9:
                    continue
                else:
                    print('Operasi tidak dikenali')
                    
            elif operasi == 2:
                print('\nLatihan/Tugas:\n1. List 1\n2. List 2\n3. Tuple\n4. Set\n5. Tugas 1\n6. Kembali')
                pilih1 = int(input('silahkan masukan pilihan (dalam angka): '))
                if pilih1 == 1:
                    p4 = Pertemuan4()
                    p4.pertemuan4_latihan1()
                elif pilih1 == 2:
                    p4 = Pertemuan4()
                    p4.pertemuan4_latihan2()
                elif pilih1 == 3:
                    p4 = Pertemuan4()
                    p4.pertemuan4_latihan3()
                elif pilih1 == 4:
                    p4 = Pertemuan4()
                    p4.pertemuan4_latihan4()
                elif pilih1 == 5:
                    p4 = Pertemuan4()
                    p4.pertemuan4_tugas2()
                elif pilih1 == 6:
                    continue
                else:
                    print('Operasi tidak dikenali')
            
            elif operasi == 3:
                print('\nLatihan/Tugas:\n1. For list\n2. For 2\n3. For Range\n4. For Break\n5. For Continue 1\n6. While Break 2\n7. While Continue Break\n8. Tugas 1\n9. Kembali')
                pilih2 = int(input('silahkan masukan pilihan (dalam angka): '))
                if pilih2 == 1:
                    p5 = Pertemuan5()
                    p5.pertemuan5_latihan1()
                elif pilih2 == 2:
                    p5 = Pertemuan5()
                    p5.pertemuan5_latihan2()
                elif pilih2 == 3:
                    p5 = Pertemuan5()
                    p5.pertemuan5_latihan3()
                elif pilih2 == 4:
                    p5 = Pertemuan5()
                    p5.pertemuan5_latihan4()
                elif pilih2 == 5:
                    p5 = Pertemuan5()
                    p5.pertemuan5_latihan5()
                elif pilih2 == 6:
                    p5 = Pertemuan5()
                    p5.pertemuan5_latihan6()
                elif pilih2 == 7:
                    p5 = Pertemuan5()
                    p5.pertemuan5_latihan7()
                elif pilih2 == 8:
                    p5 = Pertemuan5()
                    p5.pertemuan5_tugas1()
                elif pilih2 == 9:
                    continue
                else:
                    print('Operasi tidak dikenali')
                    
            elif operasi == 4:
                print('\nLatihan/Tugas:\n1. Hello world\n2. Parameter 1\n3. Parameter 2\n4. Barang\n5. Hitung\n6. Gaji\n7. Tugas 1\n8. Kembali')
                pilih3 = int(input('silahkan masukan pilihan (dalam angka): '))
                if pilih3 == 1:
                    p6 = Pertemuan6()
                    p6.pertemuan6_latihan1()
                elif pilih3 == 2:
                    p6 = Pertemuan6()
                    p6.pertemuan6_latihan2()
                elif pilih3 == 3:
                    p6 = Pertemuan6()
                    p6.pertemuan6_latihan3()
                elif pilih3 == 4:
                    p6 = Pertemuan6()
                    p6.pertemuan6_latihan4()
                elif pilih3 == 5:
                    p6 = Pertemuan6()
                    p6.pertemuan6_latihan5()
                elif pilih3 == 6:
                    p6 = Pertemuan6()
                    p6.pertemuan6_latihan6()
                elif pilih3 == 7:
                    p6 = Pertemuan6()
                    p6.pertemuan6_tugas1()
                elif pilih3 == 8:
                    continue
                else:
                    print('Operasi tidak dikenali') 
            
            elif operasi == 5:
                print('\nLatihan/Tugas:\n1. Class 1\n2. Class 2\n3. str 2\n4. Tugas 1\n5. Kembali')
                pilih4 = int(input('silahkan masukan pilihan (dalam angka): '))
                if pilih4 == 1:
                    p7 = Pertemuan7()
                    p7.pertemuan7_latihan1()
                elif pilih4 == 2:
                    p7 = Pertemuan7()
                    p7.pertemuan7_latihan2()
                elif pilih4 == 3:
                    p7 = Pertemuan7()
                    p7.pertemuan7_latihan3()
                elif pilih4 == 4:
                    p7 = Pertemuan7()
                    p7.pertemuan7_tugas1()
                elif pilih4 == 5:
                    continue
                else:
                    print('Operasi tidak dikenali')
            
            elif operasi == 6:
                print('\nLatihan/Tugas:\n1. Encapsulation \n2. Kembali')
                pilih5 = int(input('silahkan masukan pilihan (dalam angka): '))
                if pilih5 == 1:
                    p8 = Pertemuan8()
                    p8.pertemuan8_latihan1()
                elif pilih4 == 2:
                    continue
                else:
                    print('Operasi tidak dikenali')
            
            elif operasi == 7:
                print('\nLatihan/Tugas:\n1. Turunan \n2. Tugas 1\n3. Kembali')
                pilih6 = int(input('silahkan masukan pilihan (dalam angka): '))
                if pilih6 == 1:
                    p9 = Pertemuan9()
                    p9.pertemuan9_latihan1()
                elif pilih6 == 2:
                    p9 = Pertemuan9()
                    p9.pertemuan9_tugas1()
                elif pilih4 == 3:
                    continue
                else:
                    print('Operasi tidak dikenali')
            
            elif operasi == 8:
                print('\nLatihan/Tugas:\n1. Poly \n2. Tugas 1\n3. Kembali')
                pilih7 = int(input('silahkan masukan pilihan (dalam angka): '))
                if pilih7 == 1:
                    p10 = Pertemuan10()
                    p10.pertemuan10_latihan1()
                elif pilih7 == 2:
                    p10 = Pertemuan10()
                    p10.pertemuan10_tugas1()
                elif pilih7 == 3:
                    continue
                else:
                    print('Operasi tidak dikenali')
            
            elif operasi == 9:
                p11 = Pertemuan11()
                p11.pertemuan11_latihan1()
            
            elif operasi == 10:
                p12 = Pertemuan12()
                p12.pertemuan12_latihan1()
            
            elif operasi == 11:
                p13 = Pertemuan13()
                p13.pertemuan13_latihan1()
            
            elif operasi == 12:
                break
            else:
                print('Operasi tidak dikenali')    
            
a = Menu()
a.pilih_pertemuan()