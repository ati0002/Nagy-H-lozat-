import gspread
import requests

gc = gspread.service_account(filename='cread.json')
macsk = []
for i in range(0, 17):
    valasz = requests.get("https://catfact.ninja/fact")
    csak = valasz.json()
    macsk.append(csak)

# kimeno = gc.create('vince.17')
kimeno = gc.open('vince.17')
# kimeno.share("smurfac00@gmail.com", perm_type="user", role="writer")
sheet = kimeno.worksheet('Sheet1')
sheet.clear()


def kiiratas(oszlop, megoldas):
    sheet = kimeno.worksheet("Sheet1")
    try:
        sheet.update(megoldas, f"{oszlop}1")
    except:
        sheet.update([megoldas], f"{oszlop}1")

#
# 1. feladat
#
#(jó)

adat = []
for i in macsk:
    adat.append([i['fact']])
kiiratas('A', adat)


#
# 2. feladat
#
#(jó)

sor = []
szavak = []
for i in adat:
    for mondat in i:
        szavak.append(mondat.split(' '))
for i in range(0, len(szavak)):
    sor.append([len(szavak[i])])
kiiratas('B', sor)


#
# 3. feladat
#
#(elvileg jó) 

szo = []
szo2 = []
for i in szavak:
    for x in i:
        if x not in szo:
            szo.append(x)
for i in szo:
    szo2.append([i])
kiiratas('C', szo2)


#
# 4. feladat
#
#(jó)

elofordulasok = []
for i in szo:
    elofor = 0  
    for x in szavak:
        for y in x:
            if y == i:
                elofor += 1
    elofordulasok.append([elofor])  

kiiratas('D', elofordulasok)

#
# 5. feladat
#
#(elvilge jó)
legyszak = []
szam0 = 0
for i in elofordulasok:
    if i[0] > szam0:
        szam0 = i[0]
for i in range(len(elofordulasok)):
    if elofordulasok[i][0] == szam0:
        legyszak.append([szo[i]])
kiiratas('E', legyszak)
