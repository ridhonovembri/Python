nilai = 1

#while statement, dont forget to increment, if not will continue 
#forever
while nilai <= 10:
   print(nilai)
   nilai+=1

print('*'*50)
#while statement with break
while nilai <= 20:
    
    if nilai == 17:
        break

    print(nilai)
    nilai+=1

print('*'*50)
#while statement with continue
while nilai <= 30:
    nilai+=1
    
    if nilai == 21:
        continue

    print(nilai)

print('*'*50)
#while statement with else
while nilai <= 40:
    nilai+=1
    print(nilai)
    
else:
    print('nilai sudah sampai', nilai)



    