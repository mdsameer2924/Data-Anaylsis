i=0;
while i<10:
    if i==5:
        i+=1
        continue
    elif i==8:
        break
    print(i+1,"finite loop")
    i+=1
else:
    print("Loops End")
