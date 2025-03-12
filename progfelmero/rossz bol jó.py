import gspread
import requests

gc = gspread.service_account(filename='cread.json')
valasz =requests.get("https://catfact.ninja/facts")
macsk = valasz.json()

#kimeno = gc.create('vince.17')
kimeno = gc.open('vince.17')
#kimeno.share("smurfac00@gmail.com",perm_type="user",role="writer")
sheet = kimeno.worksheet('Sheet1')
sheet.clear()


def kiiratas(oszlop,megoldas,):
    sheet = kimeno.worksheet("Sheet1")
    try:
        sheet.update(megoldas,f"{oszlop}1")
    except:
        sheet.update([[megoldas]],f"{oszlop}1")


#
#1. feladat
#

adat=[]
for i in macsk['data']:
    fact = i['fact']
    mondatok = fact.split('. ')
    for mondat in mondatok:
        if mondat:
            adat.append([mondat.strip()])
            
kiiratas('A',adat)

#
#2. feladat
#

megold = []

for i in adat:
    for mondat in i: 
        szavak = mondat.split(' ')  
        megold.append([len(szavak)])  

kiiratas('B', megold)

#
#3. feladat
#

szo = []
szo2 = []
for mondat in szavak:
    for x in mondat:
        if x not in szo: 
            szo.append(x) 
for i in szo:
    szo2.append([i])

kiiratas('C', szo2)

#
#4. feladat
#

elofordulasok = []

for i in szo:
    elofordulas = 0
    for x in szavak:
        for y in x:
            if y == i:
                elofordulas += 1
    elofordulasok.append([elofordulas])

kiiratas('D', elofordulasok)

#
#5. feladat
#

#
# 5. feladat
#

legn_gyak = 0
leggyakszo = []

for i in szo:  # A "szo" lista tartalmazza az egyedi szavakat
    gyakorisag = 0
    for x in szavak:  # "szavak" lista tartalmazza az összes szót
        for y in x:
            if y == i:
                gyakorisag += 1

    if gyakorisag > legn_gyak:
        legn_gyak = gyakorisag
        leggyakszo = [[i]]  # Új lista létrehozása az új maximumhoz
    elif gyakorisag == legn_gyak:
        leggyakszo.append([i])  # Hozzáadjuk a listához, ha ugyanannyi

kiiratas('E', leggyakszo)


