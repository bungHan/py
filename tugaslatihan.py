from texttable import Texttable #import dulu texttable dari library
x = Texttable ()
j = "y"  #untuk variabel bebas ya.. 
ni = []   #pertama kita buat list kosong untuk menampung masukan
no = 0
na = []
n_t = []
n_u = []
n_us = []
while j == "y": #perintah untuk melakukan pengulangan
    na.append(input("Nama         :"))  #nama variabel ditambahkan append gunanya untuk menambahkan nilai masukan ke dalam list
    ni.append(input("NIM          :"))
    n_t.append(input("Nilai Tugas  :"))
    n_u.append(input("Nilai UTS    :"))
    n_us.append(input("Nilai UAS    :"))
    j = input("Tambah data (y/t)?")
    no += 1 #agar no nya terus bertambah 1 ketika melakukan pengulangan
for i in range(no):      
    t = int(n_t[i])          
    ut = int(n_u[i])         
    u = int(n_us[i])
    ak = t*30/100 + ut*35/100 + u*35/100   #mengulang fungsi
    x.add_rows([['No','Nama','NIM','Tugas','UTS','UAS','Akhir'],
               [i+1, na[i],ni[i],n_t[i],n_u[i],n_us[i],ak]])        #menambahkan tabel                                                                                                                                                                                                                                                                                                                                            

print (x.draw()) #menampilkan tabel