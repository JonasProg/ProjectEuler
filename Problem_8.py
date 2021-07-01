from pip._vendor.distlib.compat import raw_input


def search_engine(Zahlenreihenfolge):
    highest_value=0
    produkt_variable = 1
    for y in range(0, len(Zahlenreihenfolge) - 12):
        for x in range(y, y + 13):
            produkt_variable = int(Zahlenreihenfolge[x]) * produkt_variable
        if produkt_variable > highest_value:
            highest_value = produkt_variable
        produkt_variable = 1
    return highest_value
print((search_engine(raw_input("Please Input Number: "))))