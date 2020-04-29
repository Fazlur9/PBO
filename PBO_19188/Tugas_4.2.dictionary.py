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


