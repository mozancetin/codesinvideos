import random
sayilar = []
kolon = 1
while(True):
    sayi = random.randint(1,49)
    if len(sayilar) == 6:
        sayilar.sort()
        print("{}. Kolon: ".format(kolon) , sayilar)
        kolon += 1
        sayilar = []
        if kolon == 9:
            break
    else:
        if not (sayi in sayilar):
            sayilar.append(sayi)
input("\nKapatmak için enter'a basın...")
