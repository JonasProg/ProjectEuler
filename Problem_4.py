def palindrome():
    largest=0
    largest_x=0
    largest_y=0
    for x in range(100, 1000):
        for y in range(100,1000):
            n = x * y
            list =[]
            list.append([int(i) for i in str(n)])
            list = list[0]
            pruefung=True
            for i in range(len(list)//2):
                if list[i] != list[-1-i]:
                    pruefung=False
            if pruefung==True and n>largest:
                largest=n
                largest_x=x
                largest_y=y
    print(largest)
    print(largest_y)
    print(largest_x)
palindrome()