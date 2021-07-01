def primenumbers(number):
    list=[]
    pruefung = 0
    b = 1
    while b <= number:
        b = b + 1
        if number % b == 0:
            for x in range(2, b):
                if b % x == 0:
                    pruefung = 1
                    break
            if pruefung == 1:
                pruefung = 0
            else:
                list.append(b)
                number = number / b
                b=b-1
    print(list)
primenumbers(600851475143)



