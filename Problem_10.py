def prime_number_counter(limit):
    counter = 0
    prime_number = 1
    pruefung = True
    while prime_number < limit:
        prime_number = prime_number +1
        for x in range(2, int(prime_number**0.5) +1):
            if prime_number % x == 0:
                pruefung = False
                break
        if pruefung == False:
            pruefung = True
        else:
            counter = counter + prime_number
    return counter
print(prime_number_counter(2000000))