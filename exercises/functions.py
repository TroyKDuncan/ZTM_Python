def highest_even(given_list):
    highest = 0
    for num in given_list:
        if num % 2 != 0:
            continue
        elif num > highest:
            highest = num
    return highest


def highest_odd(given_list):
    odds = []
    for n in given_list:
        if n % 2 != 0:
            odds.append(n)
    return max(odds)


my_list = [10, 2, 3, 4, 8, 11]
print(highest_even(my_list))
print(highest_odd(my_list))
