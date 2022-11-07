vardnica = {
    "Ķīna" : "1394 410 000",
    "ASV" : "328 626 000",
    "Indija" : "1342 950 000",
    "Brazīlija" : "210 194 000",
    "Japāna" : "126 320 000",
    "Filipīnas" : "107 145 000",
    " Meksika" : "126 577 691",
    " Ēģipte" : "98 245 100",
    "Vācija" : "82 887 000",
    "Francija" : "66 992 000",
    " Latvija" : "1893 700",

}

print(vardnica,".")
    

        
for key, value in vardnica.items():
    print(f"{key} - {value}")

n = int(input("Vai jūs velaties papildinat šo vardnīcu ar vēl kadu valsti(JĀ -1; NĒ - 2)") )   

if n == 1:
    m = input("Ievadiet valsti un iedzīvotaju skatu šadi{'valsts' : 'iedzīvotāju skaits'}" )
    vardnica.update(m)
else:
    print("paldies par atbildi")    

k = int(input("Vai jūs velaties dzēt kādu valsti no šis vārdnīcas (JĀ -1; NĒ - 2)") ) 

if k == 1:
    h = input("Ievadiet valsts nosaukumu kuru vēlaties dzēst"  )
    vardnica.pop(h)
else:
    print("paldies par atbildi")   

 

print(f"Vismazāk iedzīvotāju ir Latvijā tie ir", vardnica["Latvija"], "iedzīvotāji")


print(f"Visvairāk iedzīvotāju ir Ķīnā tie ir", vardnica["Ķīna"], "iedzīvotāji")

    
