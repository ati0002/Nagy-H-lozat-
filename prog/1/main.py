ures=[]
with open("ora.txt","r",encoding="utf-8") as forras:
    for sor in forras:
        ures.append(sor.strip())

valami1={}
valami2=[]
for elem in ures:
    valami1_ures=elem.split()
    valami1["tantargy"]=valami1_ures[0]
    valami1["oraszam"]=valami1_ures[1]
    if valami1_ures[2] =="igen":
        valami1["volte"] = True
    else:
        valami1["volte"] = False
    valami1["napok"] = valami1_ures[3].split(",")
    valami1["jegyek"] = valami1_ures[4].split(",")
    valami2.append(valami1)
    valami1={} 
#1
keddi_tantargyak = [item["tantargy"] for item in valami2 if "Kedd" in item["napok"]]
print("Kedden a következő tantárgyak vannak:", keddi_tantargyak)

#3
hany=0
if valami2[0]["volte"] ==True:
    hany+=1
if valami2[1]["volte"] ==True:
    hany+=1
if valami2[2]["volte"] ==True:
    hany+=1   
if valami2[3]["volte"] ==True:
    hany+=1
if valami2[4]["volte"] ==True:
    hany+=1
if valami2[5]["volte"] ==True:
    hany+=1
print(hany)

#4
for i in range(100,0,-1):
    for tantargy in valami2:
        if len(tantargy["jegyek"])==i:
            print(f"Tantárgy: {tantargy['tantargy']}, Jegyek száma: {len(tantargy['jegyek'])}")