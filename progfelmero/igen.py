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


# 1. feladat
adat = []
for i in macsk:
    adat.append([i['fact']])
kiiratas('A', adat)

# 2. feladat
szamok = []
szavak = []
for i in adat:
    for mondat in i:
        szavak.append(mondat.split(' '))
for i in range(0, len(szavak)):
    szamok.append([len(szavak[i])])
kiiratas('B', szamok)

# 3. feladat
szo = []
szo2 = []
for i in szavak:
    for x in i:
        if x not in szo:
            szo.append(x)
for i in szo:
    szo2.append([i])
kiiratas('C', szo2)

# 4. feladat
elofordulasok = []
elofordulas = 0
for i in szo:
    for x in szavak:
        for y in x:
            if y == i:
                elofordulas += 1
    elofordulasok.append([elofordulas])
    elofordulas = 0
kiiratas('D', elofordulasok)

# 5. feladat
leggyakoribb = []
szam = 0
szam2 = 0
for i in elofordulasok:
    if i[0] > szam2:
        szam2 = i[0]
for i in range(0, len(elofordulasok)):
    if elofordulasok[i][0] == szam2:
        szam += i
leggyakoribb.append([szo[szam]])
kiiratas('E', leggyakoribb)
