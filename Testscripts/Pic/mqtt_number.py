anzahl = open("number.txt").read()
print(anzahl)
type(anzahl)
nummer=int(anzahl)
nummer=nummer+1
print(nummer)
bennenung= str(nummer)

file=open("number.txt","w")
file.write(bennenung)
file.close()

file = open("picture" + bennenung + ".txt", 'w')
