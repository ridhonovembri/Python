#loop from list
list_buah = ["pisang", "jeruk", "pepaya", "apel"]

for buah in list_buah:
    print(buah)

print('*'*50)

#loop from range
for x in range(11):
    print(x)

print('*'*50)

#loop from speficif range
for x in range(0,11,2):
    print(x)  

print('*'*50)  
    
#loop with break statement
for x in range(11):
    if x==7:
        break

    print(x)

print('*'*50)    

#loop with continue statement
for x in range(11):
    if x==7 :
        continue

    print(x)

print('*'*50)

#loop with else
for x in range(11):
    if x==7:
       continue

    print (x)
else:
    print('finished')

print('*'*50)

#nested loop
list_color = ["red","yellow","blue"]
list_fruit = ["apple","banana","greeps"]

for x in list_color:
    for y in list_fruit:
        print(x,y)



