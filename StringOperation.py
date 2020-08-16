#length of string
nilai_string = 'Hello World'
print(len(nilai_string))

#string are arrays
print('huruf kedua dari kata "Hello World" adalah :', 
       nilai_string[1])

#string slicing
print('pengambilan huruf dari kata "Hello World" adalah :', nilai_string[0:5])
print('pengambilan huruf dari kata "Hello World" adalah:',  nilai_string[-3:-1])

#string method
#remove any white space
print('menghilangkan space dari kata "Hello World":', nilai_string.strip())

#lower case
print('membuat huruf menjadi kecil:', nilai_string.lower())

#upper case
print('membuat huruf menjadi besar:', nilai_string.upper())

#replace character
print('me-replace hurf L menjadi Y pada tulisan "Hello World"', nilai_string.replace("l","y"))

#split string
print("men-split string 'Hello World':", nilai_string.split(' '))

#Check string contains
print("me-ngecek kata 'Hello World':", 'ox' not in nilai_string)

#format string
print("my name is {}, my age is {}".format('ridho', 38))


