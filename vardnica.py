"""
Vārdnīca
"""
suns ={
    "Šķirne" : "Laika",
     "Krāsa" : "Melna",
     "Svars" : "27kg",
     "Vārds" : "Čaika",
     "dzimums" : "meitene"
}

print(suns)
#print(type(suns))

print(suns["Šķirne"])
print(suns.keys())
print(suns.get("Šķirne"))
print("\n")

for key, value in suns.items():
    print(f"{key} - {value}")

for key in suns.keys():
    print(f"{key}")    

print(f"Manu suni sauc {suns['Vārds']}.Viņas šķirne ir {suns['Šķirne']}. {suns['Vārds']} ir {suns['Krāsa']} krāsas kažoks, sver {suns['Svars']}.  ") 

s = suns.copy()

suns.pop("dzimums")    
print(suns)
suns.update({"Vecums": "3gadi"})
print(suns)
print(s)
s.update({"Vecums": "3gadi"})
print(s)

for key, value in s.items():
    print(f"{key} - {value}")

for value in suns.values():
    print(f"{value}")      