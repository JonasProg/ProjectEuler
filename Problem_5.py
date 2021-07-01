def bruteForce(number):
    result = 0
    pruefung = True
    while pruefung:
        pruefung = False
        result += 1
        for x in range(1,number + 1):
            if result % x != 0:
                pruefung = True
    return result

def primeFactors(number):
    liste = []
    teiler = 1
    while number > 1:
        teiler += 1
        while (number % teiler == 0):
            liste.append(teiler)
            number /= teiler
    return liste


def besser(number):
    primeFactorList = []
    for x in range(2, number + 1):
        liste = primeFactors(x)
        for y in liste:
            while liste.count(y) > primeFactorList.count(y):
                primeFactorList.append(y)
    result = 1
    for x in primeFactorList:
        result = result * x
    return result


print(besser(20))