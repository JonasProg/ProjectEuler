def pythagorean_triplet():
    for a in range(1, 333):
        for b in range(a, 500):
            c = 1000 - b - a
            if a + b + c == 1000:
                if a < b < c and a **2 + b**2 == c**2:
                    return a,b,c
print(pythagorean_triplet())