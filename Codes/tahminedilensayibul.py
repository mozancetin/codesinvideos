import random
n=random.randint(1,100)
c=1
while(True):
    tahmin=int(input("Tahmin et: "))
    if tahmin==n:
        print("Aklımdan tuttuğum sayı: ",n)
        print("Tebrikler",c,"adımda buldunuz!")
        break
    elif tahmin>n:
        print("Daha küçük bir sayı söylemelisin\n")
        c=c+1
    else:
        print("Daha büyük bir sayı söylemelisin\n")
        c=c+1
input()
