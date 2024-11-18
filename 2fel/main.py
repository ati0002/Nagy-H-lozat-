ures=[]
with open("D:/Tanulók/Vince Attila/programozás/2fel/taborok.txt","r",encoding="utf-8") as forras:
    for sor in forras:
        ures.append(sor.strip())
lista=[]
tabor={}
jelent=[]
for elem in ures:
    tabor_ures =elem.split()
    tabor["khonap"] = tabor_ures[0]
    tabor["knap"] = tabor_ures[1]
    tabor["zhonap"] = tabor_ures[2]
    tabor["znap"] = tabor_ures[3]
    for igen in tabor_ures[4]:
         lista.append(igen)
    tabor["diakok"] = lista
    lista=[]
    tabor["tema"] = tabor_ures[5]
    jelent.append(tabor)
    tabor={}
#print(jelent)

#2
print(f"Az adatsorok száma:{len(jelent)}")
print(f"{jelent[0]["tema"]}")
