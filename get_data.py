import requests
import time

filePath = "Z:\Dev\RS_GE\data\data2.txt"

r = requests.get('https://oldschool.runescape.wiki/w/Module:GEVolumes/data?action=raw')
a = r.text
a = a.split('\n')
a = [x.strip() for x in a[1:len(a)-1]]

volumeData = {}
for elem in a:
    elem = ''.join([c for c in elem if c not in '["%,]\''])
    elem = elem.split(' = ')
    volumeData[elem[0]] = elem[1]

r = requests.get('https://oldschool.runescape.wiki/w/Module:GEPrices/data?action=raw')
a = r.text
a = a.split('\n')
a = [x.strip() for x in a[1:len(a) - 1]]

bondValue = ""
lastUpdated = ""

priceData = {}
for elem in a:
    elem = ''.join([c for c in elem if c not in '["%,]\''])
    elem = elem.split(' = ')
    priceData[elem[0]] = elem[1]


mostTaxedItem = requests.get("https://services.runescape.com/m=itemdb/obj_sprite.gif?id=X")


tax = 0
for item in volumeData.keys():
    if "LAST_UPDATE" in item:
        lastUpdated = volumeData["LAST_UPDATE"]
        continue
    if "Old school bond" in item:
        bondValue = priceData[item]
        continue

    price = int(priceData[item])
    volume = int(volumeData[item])

    if price <= 100:
        continue
    elif price >= 500000000:
        currItemTax = 5000000
    else:
        currItemTax = (price *.01) * volume
    tax += currItemTax









with open(filePath,'a') as fd:
    print(str(round(tax)))
    print(lastUpdated)
    print(bondValue)
    newRow ="\n"+ str(round(tax)) +":"+str(round(time.time()))
    fd.write(newRow)
