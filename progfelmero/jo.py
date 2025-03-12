import requests
import gspread

gc = gspread.service_account(filename='creds.json')

resp = requests.get('https://catfact.ninja/facts')
macska_infok = resp.json()

#kimeno = gc.create('laczko.17')
kimeno = gc.open('laczko.17')
#kimeno.share('nigen789@gmail.com',perm_type='user',role='writer')
worksheet = kimeno.worksheet("Sheet1")
worksheet.clear()


def kiiratas(oszlop,megoldas,):
    worksheet = kimeno.worksheet("Sheet1")
    try:
        worksheet.update(megoldas,f"{oszlop}1")
    except:
        worksheet.update([megoldas],f"{oszlop}1")
    return print('kész')

#1 feladat
adat=[]
for i in macska_infok['data']:
    adat.append([i['fact']])
kiiratas('A',adat)

#2 feladat
szamok=[]
szavak=[]
for i in adat:
    for x in i:
        szavak.append(x.split(' '))
for i in range (0,len(szavak)):
    szamok.append([len(szavak[i])])
kiiratas('B',szamok)

#3 feladat
mindenszoegyszer=[]
mindenszoegyszer2=[]
for i in szavak:
    for x in i:
        if x not in mindenszoegyszer:
            mindenszoegyszer.append(x)
for i in mindenszoegyszer:
    mindenszoegyszer2.append([i])
kiiratas('C',mindenszoegyszer2)

#4 feladat
elofordulasok=[]
elofordulas=0
for i in mindenszoegyszer:
    for x in szavak:
        for y in x:
            if y == i:
                elofordulas+=1
    elofordulasok.append([elofordulas])
    elofordulas=0
kiiratas('D',elofordulasok)

#5 feladat
leggyakoribb=[]
szam=0
max=0
for i in elofordulasok:
    if i[0] > max:
        max=i[0]
for i in range(0,len(elofordulasok)):
    if elofordulasok[i][0] == max:
        szam+=i
leggyakoribb.append([mindenszoegyszer[szam]])
kiiratas('E',leggyakoribb)
