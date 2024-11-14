ures=[]
with open("bedat.txt","r",encoding="utf-8") as forras:
    print(forras)
    for sor in forras:
        ures.append(sor.strip())
        
igen={}
nem=[]
for adat in ures:
    igen_ures = adat.split() 
    igen["AZ"] = igen_ures[0]
    igen["Óra"] = igen_ures[1].split(":")
    igen["Azonositó"] = igen_ures[2]
    nem.append(igen)
    igen={}
#print(nem)

#3
asd={}
dsa=[]
for i in nem:
    if int(i["Óra"][0]) == 7 and int(i["Óra"][1]) >= 51 and int(i["AZ"]) == 1 : 
        asd["ora"] = i["Óra"][0]
        asd["perc"] = i["Óra"][1]
        asd["azon"] = i["AZ"]
        dsa.append(asd)
        dsa={}   
    if int(i["Óra"][0]) == 8 and int(i["Óra"][1]) <= 15 and int(i["AZ"]) == 1 :
        asd["ora"] = i["Óra"][1]
        asd["perc"] = i["Óra"][1]
        asd["azon"] = i["AZ"]
        dsa.append(asd)
        dsa={}
print(dsa)