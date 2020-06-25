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

