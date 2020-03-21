import random

liste = [1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
mac = []

for i in range(6):

    a = random.choice(liste)
    b = random.choice(liste)

    ikili = str(a) + str(b)
    mac.append(ikili)
    ikili = None

mac_adresi = mac[0] + ":" + mac[1] + ":" + mac[2] + ":" + mac[3] + ":" + mac[4] + ":" + mac[5]
print(mac_adresi)

input()
