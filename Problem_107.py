import numpy as np

def line_counter():
    # Opening a file
    file = open('C:\\Users\\Jonas\\GitHub_Kurs_Rep\\My_Scientific_Software_Developement\\small_matrix.txt',"r")
    Counter = 0
  
    # Reading from file
    Content = file.read()
    CoList = Content.split("\n")
  
    for i in CoList:
        if i:
            Counter += 1
    return Counter
def minimal_network():
    matrix_file= open('C:\\Users\\Jonas\\GitHub_Kurs_Rep\\My_Scientific_Software_Developement\\small_matrix.txt')
    list_matrix=[]
    for x in range(0,line_counter()):
        zeile= matrix_file.readline()
        zeile= zeile.strip()
        spalten= zeile.split(",")
        for y in spalten:
            list_matrix.append(y)
    Aarray_matrix=np.array(list_matrix)
    Barray_matrix =  np.reshape(Aarray_matrix, (-1, line_counter()))

    print(Barray_matrix)
    print(Barray_matrix[6,3])
print(minimal_network())