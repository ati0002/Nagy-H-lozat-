adat=[]
with open("bedat.txt","r",encoding="utf-8") as forras:
    for sor in forras:
        adat.append(sor.strip())
belepes={}
belepesitabla=[]
for elem in adat:
    belepes_adat = elem.split()
    belepes["szazonosito"] = belepes_adat[0]
    belepes["ido"] =  belepes_adat[1].split(":")
    belepes["bazonosito"] = belepes_adat[2]
    belepesitabla.append(belepes)
    belepes={}
#2
elso=24
elsop=60
utolso=0
utolsop=0
for b in belepesitabla:
    if elso > int(b["ido"][0]) and int(b["bazonosito"]) == 1:
        elso = int(b["ido"][0])
    if utolso < int(b["ido"][0]) and int(b["bazonosito"]) == 2:
        utolso = int(b["ido"][0])
for a in belepesitabla:
    if elsop > int(a["ido"][1]) and int(a["bazonosito"]) == 1 and elso == int(a["ido"][0]):
        elsop = int(a["ido"][1])
    if utolsop < int(a["ido"][1]) and int(a["bazonosito"]) == 2 and utolso == int(a["ido"][0]):
        utolsop = int(a["ido"][1])
print(f"{elso}:{elsop}")
print(f"{utolso}:{utolsop}")


#3
keso={}
kesok=[]
for i in belepesitabla:
    if int(i["ido"][0]) == 7 and int(i["ido"][1]) > 50 and int(i["bazonosito"]) == 1:
        keso["ora"] = i["ido"][0]
        keso["perc"] = i["ido"][1]
        keso["azon"] = i["szazonosito"]
        kesok.append(keso)
        keso={}
    if int(i["ido"][0]) == 8 and int(i["ido"][1]) <= 15 and int(i["bazonosito"]) == 1:
        keso["ora"] = i["ido"][0]
        keso["perc"] = i["ido"][1]
        keso["azon"] = i["szazonosito"]
        kesok.append(keso)
        keso={}
#print(kesok)

with open("kesok.txt","w",encoding="utf-8") as kimeno:
    for x in kesok:
        kimeno.write(str(x["ora"])+":")
        kimeno.write(str(x["perc"])+" ")
        kimeno.write(str(x["azon"])+"\n")

#4
ebedlok=0
for y in belepesitabla:
    if int(y["bazonosito"]) == 3:
        ebedlok+=1
print(ebedlok)

#5.1
kjarok=[]
for z in belepesitabla:
    if int(z["bazonosito"]) == 4 and z["szazonosito"] not in kjarok:
        kjarok.append(z["szazonosito"])
print(len(kjarok))

#5.2
if ebedlok > len(kjarok):
    print("Nem voltak többen mint a menzások")
if ebedlok < len(kjarok):
    print("Többen voltak mint a menzások")

#6
szokok=[]
nemvisszaerok=[]
for c in belepesitabla:
    if int(c["ido"][0]) == 10 and 45 <= int(c["ido"][1]) < 50 and int(c["bazonosito"]) == 2:
        szokok.append(c["szazonosito"])
for d in belepesitabla:
    if int(d["ido"][0]) == 10 and 50 <= int(d["ido"][1]) < 59 and int(d["bazonosito"]) == 1:
        nemvisszaerok.append(d["szazonosito"])
print(nemvisszaerok)

#7

igen=[]
for aa in belepesitabla:
    if aa["szazonosito"] not in igen:
        igen.append(aa["szazonosito"])
        
bo=24
bp=60
ko=0
kp=0
keszo=0
keszp=0
for ab in belepesitabla:
    for az in igen:
        if ab["szazonosito"] == az and int(ab["bazonosito"]) == 1 and bo > int(ab["ido"][0]):
            bo =int(ab["ido"][0])
        if ab["szazonosito"] == az and int(ab["bazonosito"]) == 1 and bp > int(ab["ido"][1]) and bo == int(ab["ido"][0]):
            bp =int(ab["ido"][1])
            
        if ab["szazonosito"] == az and int(ab["bazonosito"]) == 2 and ko < int(ab["ido"][0]):
            ko =int(ab["ido"][0])
        if ab["szazonosito"] == az and int(ab["bazonosito"]) == 2 and kp < int(ab["ido"][1]) and ko == int(ab["ido"][0]):
            kp =int(ab["ido"][1])
    keszo=ko-bo
    keszp=kp-bp  
    print(f"{ab} {keszo} órak és {keszp} percet töltött az isolában")
    bo=24
    p=60
    ko=0
    kp=0
   