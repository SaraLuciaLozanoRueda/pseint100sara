XN =7
f=1

for f in range (1,7):
    serie= ""
    if f >= 5:
        XN = XN + 2
    c=1
    for c in range (1,XN +1 -f):
        serie= str (serie)+ str (" * ")

    print (serie)
