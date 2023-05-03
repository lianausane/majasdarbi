vārdnīca ={
    "kaķis" : "cat",
    "suns" : "dog",
    "zivs" : "fish",
    "varde" : "frog",
    "čūska" : "snake",
    "pele" : "mouse",
    "māsa" : "sister",
    "roze" : "rose",
    "telefons" : "phone",
    "ola" : "egg",
    "gailis" : "rooster",
    "lampa" : "lamp",
    "vīrietis" : "man",
    "lapsa" : "fox",
    "sieviete" : "women",
    "skudra" : "ant",
    "pica" : "pizza",
    "kūka" : "cake",
    "saldējums" : "ice creame",
    "giesti" : "ceiling",
}
import random

print(random.choice(list(vārdnīca.values())))

for key, value in vārdnīca.items():
    print(f"{key} - {value}")

l = [ ]

for key in vārdnīca.keys():
    l.append(key)

#print(l)

for key in vārdnīca.keys():
    print(f"{key}")

#n = str(input("Ievadiet vārdu latviski no datajiem vardiem kuru vēlaties tulkot uz angļu valodu. "))
#print(vārdnīca[n])

v = str(input("Ievadiet vienu no dotajiem vārdiem, kuru vēlaties iztulkot: "))
print(vārdnīca[v])

print("Vai vēlaties iztulkot vēl kādu vārdu?")
k = int(input("Atbilžu varianti: 1-Jā; 2-Nē: " ))

if k == 1:
    m = int(input("Cik vārdus vēlaties vēl iztulkot? ")) 
    for i in range (m):
        v = str(input("Ievadiet vienu no dotajiem vārdiem, kuru vēlaties iztulkot: "))
        print(vārdnīca[v])
    print("Paldies, ka izmantojāt tulkotāju! ")
else:
    print("Paldies, ka izmantojāt tulkotāju! ")

keys_list = list(vārdnīca)
key = keys_list[0]
print(key)
  
  