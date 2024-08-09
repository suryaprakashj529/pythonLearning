def positive_even_squares(*args):
    # Write your code here.
    positive_even_nums = []

    for lst in args:
        filtered_list = filter(lambda x:x > 0 and x %2 == 0, lst)
        positive_even_nums.extend(filtered_list)

    squares = map(lambda x:x ** 2, positive_even_nums)
    return list(squares)
