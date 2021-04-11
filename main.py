import natiogeo
from time import sleep
f = open('url.txt', 'r' ,encoding='utf-8-sig')
datalist = f.readlines()
out = ""
for url in datalist:
    out += natiogeo.natiogeoload(url.replace( '\n' , '' ))
    sleep(10)
f.close()
with open('import.txt','w', newline='', encoding='utf-8') as f:
    f.write(out)