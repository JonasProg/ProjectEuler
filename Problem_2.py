def fibonacci(maximum):
    Sum=0
    letzte_zahl=2
    vorletzte_zahl=1
    while letzte_zahl<=maximum:
        nachste_zahl=letzte_zahl+vorletzte_zahl
        vorletzte_zahl=letzte_zahl
        letzte_zahl=nachste_zahl
        if vorletzte_zahl%2 == 0:
            Sum=Sum+vorletzte_zahl
    return Sum
print(fibonacci(4000000))

