nilai_int = 10
nilai_string = 'nilai string'
nilai_float = 10.5
nilai_bool = True

nilai_1, nilai_2, nilai_3 = "satu", "dua", "tiga"

nilai_4 = nilai_5 = nilai_6 = "ini nilainya sama"

var_global = "nilai global"

var_str_multipleLine = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""  

print(nilai_int)
print(nilai_string)
print(nilai_float)
print(nilai_bool)
print(nilai_int + nilai_float)

print(nilai_1)
print(nilai_2)
print(nilai_3)

print(nilai_4)
print(nilai_5)
print(nilai_6)

def getVarGlobal():
    global var_global     
    var_global = "ini dalam function"
    print("nilai var global :", var_global)

getVarGlobal()

print(var_global)

print(var_str_multipleLine)