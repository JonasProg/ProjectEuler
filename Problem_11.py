def txt_reader():
    file = open('C:\\Users\\Jonas\\Desktop\\Python_Matrix.txt')
    liste = file.readlines()
    liste2 = []
    final_liste=[]
    for x in range(0, len(liste)):
        liste2 = liste[x].split()
        liste2 = [int(i) for i in liste2]
        final_liste.append(liste2)
    return final_liste

def greatest_product():
    import_liste = txt_reader()
    horizontal_product=1
    vertical_product=1
    diagonal_product=1
    diagonal_product2 = 1
    great_product = 0
    #4 adjacent horizontal numbers
    for a in range(0, len(import_liste)):
        for b in range(0, len(import_liste[a])-3):
            for c in range(b,b+4):
                horizontal_product = horizontal_product * import_liste[b][c]
                if horizontal_product > great_product:
                    great_product = horizontal_product
            horizontal_product = 1
    #4 adjacent vertical numbers
    for d in range(0, len(import_liste)-3):
        for e in range(0, len(import_liste[d])):
            for f in range(d,d+4):
                vertical_product = vertical_product * import_liste[f][e]
                if vertical_product > great_product:
                    great_product = vertical_product
            vertical_product = 1
    #4 adjacent diagonal numbers downwards right to left
    for g in range(0, len(import_liste)-3):
        for h in range(3, len(import_liste[g])):
            for i in range(0,4):
                diagonal_product = diagonal_product * import_liste[g+i][h-i]
                if diagonal_product > great_product:
                    great_product = diagonal_product
            diagonal_product = 1
    #4 adjacent diagonal numbers downwards left to right
    for g in reversed(range(0, len(import_liste)-3)):
        for h in range(0, len(import_liste[g])-3):
            for i in range(0,4):
                diagonal_product2 = diagonal_product2 * import_liste[g+i][h+i]
                if diagonal_product2 > great_product:
                    great_product = diagonal_product2
            diagonal_product2=1
    return great_product

print(greatest_product())