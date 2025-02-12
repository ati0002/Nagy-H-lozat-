import gspread

gc = gspread.service_account(filename='creds.json')

#kimeno = gc.create('auto3')
kimeno = gc.open('auto3')
#kimeno.share('zoltanorosz792@gmail.com',perm_type='user',role='writer')
#kimeno.share('nigen789@gmail.com',perm_type='user',role='writer')

feladatszam = 0

def kiiratas(feladatszam, megoldas):

    feladatszam = feladatszam + 1
    try:
        worksheet = kimeno.worksheet(f"{feladatszam}-feladat")
        worksheet.clear()
    except:
        kimeno.add_worksheet(title=f"{feladatszam}-feladat", rows=100, cols=20)
        worksheet = kimeno.worksheet(f"{feladatszam}-feladat")
    try:
        worksheet.update(megoldas, "A1")
    except:
        worksheet.update([megoldas], "A1")
    return feladatszam


fejlec = []
adat = []
with open('autotabla.txt', 'r', encoding='utf-8') as forras:
    for sor in forras:
        adat.append(sor.strip())

fejlec = adat[0].split(',')
adat.pop(0)

autok = {}
autoktabla = []
for elem in adat:
    auto_adat = elem.split(',')
    for i in range(0, 3):
        autok[fejlec[i]] = auto_adat[i]
    for i in range(3, 10):
        autok[fejlec[i]] = int(auto_adat[i].replace('-', ''))
    autoktabla.append(autok)
    autok = {}

# 1. feladat
automarkak = []
automarkak2 = []
automarkak2.append([fejlec[1]])
for i in autoktabla:
    if i[fejlec[1]] not in automarkak:
        automarkak.append(i[fejlec[1]])
for i in automarkak:
    automarkak2.append([i])
feladatszam = kiiratas(feladatszam, automarkak2)

# 2. feladat
gyartasievek = []
gyartasievek2 = []
gyartasievek2.append([fejlec[3]])
for i in autoktabla:
    if i[fejlec[3]] not in gyartasievek:
        gyartasievek.append(i[fejlec[3]])
for i in gyartasievek:
    gyartasievek2.append([i])
feladatszam = kiiratas(feladatszam, gyartasievek2)

# 3. feladat
minimumkilometer = []
minimumkilometerek = []
minimumkilometerek.append([fejlec[3], fejlec[6]])
kiskm = 999999
for i in gyartasievek:
    for x in autoktabla:
        if i == x[fejlec[3]] and kiskm > x[fejlec[6]]:
            kiskm = x[fejlec[6]]
    minimumkilometer.append(i)
    minimumkilometer.append(kiskm)
    minimumkilometerek.append(minimumkilometer)
    kiskm = 999999
    minimumkilometer = []
feladatszam = kiiratas(feladatszam, minimumkilometerek)

# 4. feladat
maximumkilometer = []
maximumkilometerek = []
maximumkilometerek.append([fejlec[1], fejlec[6]])
maxkm = 0
for i in automarkak:
    for x in autoktabla:
        if i == x[fejlec[1]] and maxkm < x[fejlec[6]]:
            maxkm = x[fejlec[6]]
    maximumkilometer.append(i)
    maximumkilometer.append(maxkm)
    maximumkilometerek.append(maximumkilometer)
    maxkm = 0
    maximumkilometer = []
feladatszam = kiiratas(feladatszam, maximumkilometerek)

# 5. feladat
szumkilometer = []
szumkilometerek = []
szumkilometerek.append([fejlec[1], fejlec[6]])
szumkm = 0
for i in automarkak:
    for x in autoktabla:
        if i == x[fejlec[1]]:
            szumkm += x[fejlec[6]]
    szumkilometer.append(i)
    szumkilometer.append(szumkm)
    szumkilometerek.append(szumkilometer)
    szumkm = 0
    szumkilometer = []
feladatszam = kiiratas(feladatszam, szumkilometerek)

# 6. feladat
legkesobbiforgalmil = []
legkesobbiforgalmilok = []
legkesobbiforgalmilok.append([fejlec[3], fejlec[4]])
legkeso = 0
for i in gyartasievek:
    for x in autoktabla:
        if i == x[fejlec[3]] and legkeso < x[fejlec[4]]:
            legkeso = x[fejlec[4]]
    legkesobbiforgalmil.append(i)
    legkesobbiforgalmil.append(legkeso)
    legkesobbiforgalmilok.append(legkesobbiforgalmil)
    legkeso = 0
    legkesobbiforgalmil = []
feladatszam = kiiratas(feladatszam, legkesobbiforgalmilok)

# 7. feladat
legkissebbhengerurtartalom = []
legkissebbhengerurtartalomak = []
legkissebbhengerurtartalomak.append([fejlec[1], fejlec[7]])
kis = 9999
for i in automarkak:
    for x in autoktabla:
        if i == x[fejlec[1]] and kis > x[fejlec[7]]:
            kis = x[fejlec[7]]
    legkissebbhengerurtartalom.append(i)
    legkissebbhengerurtartalom.append(kis)
    legkissebbhengerurtartalomak.append(legkissebbhengerurtartalom)
    kis = 9999
    legkissebbhengerurtartalom = []
feladatszam = kiiratas(feladatszam, legkissebbhengerurtartalomak)

# 8. feladat
modell = []
modellm = []
modellek = []
modellek.append([fejlec[1], fejlec[2]])
szam = 0
for i in automarkak:
    modell.append(i)
    for x in autoktabla:
        if i == x[fejlec[1]] and x[fejlec[2]] not in modell:
            modell.append(x[fejlec[2]])
            szam += 1
    modellm.append(i)
    modellm.append(szam)
    modellek.append(modellm)
    modellm = []
    modell = []
    szam = 0
feladatszam = kiiratas(feladatszam, modellek)

# 9. feladat
atlagkilometer = []
atlagkilometerek = []
atlagkilometerek.append([fejlec[1], fejlec[6]])
atlagkmsz = 0
szam = 0
for i in automarkak:
    for x in autoktabla:
        if i == x[fejlec[1]]:
            atlagkmsz += x[fejlec[6]]
            szam += 1
    atlagkm = atlagkmsz / szam
    atlagkilometer.append(i)
    atlagkilometer.append(atlagkm)
    atlagkilometerek.append(atlagkilometer)
    atlagkmsz = 0
    szam = 0
    atlagkilometer = []
feladatszam = kiiratas(feladatszam, atlagkilometerek)

# 10. feladat
osszkm = 0
osszkmki = []
osszkmki.append([fejlec[6]])
for i in autoktabla:
    osszkm += i[fejlec[6]]
osszkmki.append([osszkm])
feladatszam = kiiratas(feladatszam, osszkmki)

# 11. feladat
atlagar1 = []
atlagarak = []
atlagarak.append([fejlec[1], fejlec[5]])
atlagarsz = 0
szam = 0
for i in automarkak:
    for x in autoktabla:
        if i == x[fejlec[1]]:
            atlagarsz += x[fejlec[5]]
            szam += 1
    atlagar2 = atlagarsz / szam
    atlagar1.append(i)
    atlagar1.append(atlagar2)
    atlagarak.append(atlagar1)
    atlagarsz = 0
    szam = 0
    atlagar1 = []
feladatszam = kiiratas(feladatszam, atlagarak)

# 12. feladat
atlaghengereknagyobb19 = []
atlaghengereknagyobb19.append([fejlec[1]])
atlaghenger = 0
szam = 0
for i in automarkak:
    for x in autoktabla:
        if i == x[fejlec[1]]:
            atlaghenger += x[fejlec[7]]
            szam += 1
    atlaghenger2 = atlaghenger / szam
    if atlaghenger2 < 1900:
        atlaghengereknagyobb19.append([i])
    atlaghenger = 0
    szam = 0
feladatszam = kiiratas(feladatszam, atlaghengereknagyobb19)

# 13. feladat
atlaghengereknagyobb2025 = []
atlaghengereknagyobb2025.append([fejlec[1]])
atlaghenger = 0
szam = 0
for i in automarkak:
    for x in autoktabla:
        if i == x[fejlec[1]]:
            atlaghenger += x[fejlec[7]]
            szam += 1
    atlaghenger2 = atlaghenger / szam
    if atlaghenger2 > 2000 and atlaghenger2 < 2500:
        atlaghengereknagyobb2025.append([i])
    atlaghenger = 0
    szam = 0
feladatszam = kiiratas(feladatszam, atlaghengereknagyobb2025)

# 14. feladat
teljesitmenytomegmarka = []
teljesitmenytomegmarkankent = []
teljesitmenytomegmarkankent.append([fejlec[1], (fejlec[9] + '/' + fejlec[8])])
teljesitmenytomeg = 0
teljesitmenytomegatlag = 0
szam = 0
for i in automarkak:
    for x in autoktabla:
        if i == x[fejlec[1]]:
            teljesitmenytomeg += x[fejlec[9]] / x[fejlec[8]]
            szam += 1
    teljesitmenytomegatlag = teljesitmenytomeg / szam
    teljesitmenytomegmarka.append(i)
    teljesitmenytomegmarka.append(teljesitmenytomegatlag)
    teljesitmenytomegmarkankent.append(teljesitmenytomegmarka)
    teljesitmenytomegmarka = []
    teljesitmenytomeg = 0
    teljesitmenytomegatlag = 0
    szam = 0
feladatszam = kiiratas(feladatszam, teljesitmenytomegmarkankent)

# 15. feladat
kevesebbkilometer65e = []
kevesebbkilometer65e.append([fejlec[3]])
minimumkilometerek.pop(0)
for i in minimumkilometerek:
    if i[1] < 65000:
        kevesebbkilometer65e.append([i[0]])
feladatszam = kiiratas(feladatszam, kevesebbkilometer65e)

# 16. feladat
nemhaladjamegakm90e = []
nemhaladjamegakm90e.append([fejlec[1]])
maximumkilometerek.pop(0)
for i in maximumkilometerek:
    if i[1] < 90000:
        nemhaladjamegakm90e.append([i[0]])
feladatszam = kiiratas(feladatszam, nemhaladjamegakm90e)

# 17. feladat
tatomanykilometer = []
tatomanykilometer.append([fejlec[1]])
szumkilometerek.pop(0)
for i in szumkilometerek:
    if i[1] > 280000 and i[1] < 320000:
        tatomanykilometer.append([i[0]])
feladatszam = kiiratas(feladatszam, tatomanykilometer)

# 18. feladat
nemharomev = []
nemharomev.append([fejlec[3]])
legkesobbiforgalmilok.pop(0)
for i in legkesobbiforgalmilok:
    if i[1] - 20250206 < 30000:
        nemharomev.append([i[0]])
feladatszam = kiiratas(feladatszam, nemharomev)

# 19. feladat
kozeesik = []
kozeesik.append([fejlec[1]])
legkissebbhengerurtartalomak.pop(0)
for i in legkissebbhengerurtartalomak:
    if i[1] > 1700 and i[1] < 1900:
        kozeesik.append([i[0]])
feladatszam = kiiratas(feladatszam, kozeesik)

# 20. feladat
haromodell = []
haromodell.append([fejlec[1]])
for i in modellek:
    if i[1] == 3:
        haromodell.append([i[0]])
feladatszam = kiiratas(feladatszam, haromodell)

# 21. feladat
nagyobbatlagfutas = []
nagyobbatlagfutas.append([fejlec[1]])
atlagkilometerek.pop(0)
for i in atlagkilometerek:
    if i[1] < 80000:
        nagyobbatlagfutas.append([i[0]])
feladatszam = kiiratas(feladatszam, nagyobbatlagfutas)

# 22. feladat
haromlekisebb = []
haromlekisebb.append([fejlec[1]])
egy = 999999
ketto = 999999
harom = 999999
atlagarak.pop(0)
for i in atlagarak:
    if egy > i[1]:
        egy = i[1]
for i in atlagarak:
    if ketto > i[1] and i[1] > egy:
        ketto = i[1]
for i in atlagarak:
    if harom > i[1] and i[1] > ketto:
        harom = i[1]
for i in atlagarak:
    if egy == i[1]:
        haromlekisebb.append([i[0]])
    if ketto == i[1]:
        haromlekisebb.append([i[0]])
    if harom == i[1]:
        haromlekisebb.append([i[0]])
feladatszam = kiiratas(feladatszam, haromlekisebb)
