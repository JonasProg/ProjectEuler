def collatz_sequence(limit):
    counter= 1
    longest_chain=0
    result = 0
    for x in range(1, limit):
        starting_number = x
        while starting_number != 1:
            if starting_number % 2 == 0:
                starting_number = starting_number / 2
                counter = counter + 1
            else:
                starting_number = starting_number *3 + 1
                counter = counter + 1
        if counter > longest_chain:
            longest_chain = counter
            result = x
        counter=1
    return longest_chain , result

print(collatz_sequence(1000000))