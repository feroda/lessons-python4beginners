#Lista
l = [1,3,7,9,10]
#Lista compression
l2 = [x*2 for x in l]
#Dizionario compressiono
d2 = {k: k*2 for k in l}
#Crea un lista di tuple composte dei elementi delle due liste (si ferma alla lista più corta)
zip(l,l2)