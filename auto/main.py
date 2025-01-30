#import gspread

#gc =gspread.service_account(filename="cread.json")

fejlec =[]
adat =[]
with open ("autok.txt","r",encoding="utf8") as forras:
    for sor in forras:
        adat.append(sor.strip())
        
fejlec.append(adat[0].strip(","))
adat.pop(0)
print(adat)

datum=[]
autok = {}
for elem in fejlec:
    autok_adat = elem.split(',')
    autok["rendszam"] = autok_adat[0]
    autok["marka"] = autok_adat[1]
    autok["modell"] = autok_adat[2]
    autok["gyartasiev"] = int(autok_adat[3])
    autok["forgalmiErvenyesseg"] = int(autok_adat[4])
    autok["vetelar"] = int(autok_adat[5])
    autok["kmallas"] = int(autok_adat[6])
    autok["hengerUrtartalom"] = int(autok_adat[7])
    autok["tomeg"] = int(autok_adat[8])
    autok["teljesitmeny"] = int(autok_adat[9])
    

    
    