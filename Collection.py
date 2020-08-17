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

#tuples (after create cannot modified)
tuples_motor = ("yamaha","honda","suzuki")
tuples_mobil  = ("toyota","daihatsu","mitsubishi")

for x in tuples_motor:
    print(x)

print('index ke 2 dari tuples_motor adalah:', tuples_motor[2])

print("join 2 tuples", tuples_motor + tuples_mobil)

print('*'*50)

#sets (cannot orderable and indexing)
sets_komputer = {"HP","DELL","Toshiba","Asus"}

for x in sets_komputer:
    print(x)

#tidak bisa akses index dari collection sets
#print(sets_komputer[1])

sets_komputer.add("Samsung")
print(sets_komputer)

print('*'*50)

#Dictionary
dict_AC = {
    'merk':'Sharp',
    'type':'sayonara',
    'watt':220
}

print(dict_AC)
print(dict_AC['merk'])
print(dict_AC.get("watt"))

for x in dict_AC:
    print('key pada dict_ac=', x)

#change value dict
dict_AC['type'] = 'tahan panas'

print(dict_AC)

for x in dict_AC:
    print('values pada dict_ac:',dict_AC[x])

for x in dict_AC.values():
    print(x)

for x,y in dict_AC.items():
    print(x,':',y)

print(len(dict_AC))

#nested dict
dict_sepeda = {
    "sepeda1":{
    "merk":"polygon",
    "gearset":"3x9"
    },
    "sepeda2":{
    "merk":"united",
    "gearset":"3x7"
    },
    "sepeda3":{
    "merk":"merida",
    "gearset":"2x10"
    }
}

print(dict_sepeda)