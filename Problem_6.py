def sum_square_difference(number):
    sum_of_square=0
    square_of_sum=0
    for x in range(1,number + 1):
        sum_of_square= sum_of_square + x**2
        square_of_sum = (x + square_of_sum)
    square_of_sum = square_of_sum**2
    return square_of_sum - sum_of_square
print(sum_square_difference(100))