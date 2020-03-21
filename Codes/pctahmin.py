import random
c=1
a=1
b=100
while(True):
    tahmin=random.randint(a,b)
    print("\n" , "Tahminim:" , tahmin , "doğru mu? \n")
    bkmk=int(input(" Daha büyükse: 1 \n Daha küçükse: -1 \n Bildiyse:0 yazın \n "))
    if bkmk==0:
        print(c,"adımda bildim!")
        break
    elif bkmk==1:
        a=tahmin+1
        c=c+1
    elif bkmk==-1:
        b=tahmin-1
        c=c+1
input()

