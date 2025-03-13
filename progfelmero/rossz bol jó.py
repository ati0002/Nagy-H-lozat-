import gspread
import requests

gc = gspread.service_account(filename='cread.json')
macsk=[]
for i in range(0, 17):
    valasz =requests.get("https://catfact.ninja/fact")
    csak=valasz.json()
    macsk.append(csak)

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
for i in macsk:
    adat.append([i['fact']])
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

szo=[]
szo2=[]
for i in szavak:
    if i not in szo:
        szo.append(i)
for i in szo:
    szo2.append([i])
kiiratas('C',szo2)

#
#4. feladat
#

elofordulasok = []

for i in szo:
    elofordulas = 0
    for mondat in adat:  
        for szo_mondatban in mondat[0].split():  
            if szo_mondatban == i:  
                elofordulas += 1  
    elofordulasok.append([elofordulas])

kiiratas('D', elofordulasok)


#
# 5. feladat
#

legn_gyak = 0
leggyakszo = []

for i in szo:  
    gyakorisag = 0
    for x in szavak:  
        for y in x:
            if y == i:
                gyakorisag += 1

    if gyakorisag > legn_gyak:
        legn_gyak = gyakorisag
        leggyakszo = [[i]]  
    elif gyakorisag == legn_gyak:
        leggyakszo.append([i])  

kiiratas('E', leggyakszo)


