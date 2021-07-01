def Multiples_3_and_5(bis_zu):
    Summe=0
    for x in range(bis_zu):
        if x % 3 == 0 or x % 5 == 0:
            Summe=Summe+x
    print(Summe)
Multiples_3_and_5(1000)
