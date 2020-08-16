#List
list_sepeda = ["polygon","united","merida","exostis","pacific"]
for x in list_sepeda:
    print(x)

print('index yang pertama', list_sepeda[0])
print('index yang kedua', list_sepeda[1])
print('index yang ketiga', list_sepeda[2])
print('index yang terakhir', list_sepeda[-1])
print('index antara 1,2,3', list_sepeda[1:4])

list_sepeda[3] = "wim cycle"
print('ganti index yang ketiga dengan ', list_sepeda[3])
print(list_sepeda)

print('cek banyaknya item:', len(list_sepeda))
list_sepeda.append('exostis')
print('tambah data:', list_sepeda)
list_sepeda.remove('merida')
print(list_sepeda)

print('*'*50)

#tuples
tuples_motor = ("yamaha","honda","suzuki")
tuples_mobil  = ("toyota","daihatsu","mitsubishi")

for x in tuples_motor:
    print(x)

print('index ke 2 dari tuples_motor adalah:', tuples_motor[2])

print("join 2 tuples", tuples_motor + tuples_mobil)

print('*'*50)

#sets
sets_komputer = {"HP","DELL","Toshiba","Asus"}

for x in sets_komputer:
    print(x)

#tidak bisa akses index dari collection sets
#print(sets_komputer[1])

sets_komputer.add("Samsung")
print(sets_komputer)