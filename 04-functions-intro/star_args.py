def sum_numbers(*values: float) -> float:
    """ calculates the sum of all the numbers passed as arguments """
    result = 0
    for number in values:
        result += number
    return result


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))


def sum_numbers2(*values: float) -> float:
    """ calculates the sum of all the numbers passed as arguments """
    return sum(values)


print(sum_numbers2(1, 2, 3))
print(sum_numbers2(8, 20, 2))
print(sum_numbers2(12.5, 3.147, 98.1))
print(sum_numbers2(1.1, 2.2, 5.5))