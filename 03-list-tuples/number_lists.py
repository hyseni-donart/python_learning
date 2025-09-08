empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

print(min(even))
print(max(even))
print(min(odd))
print(max(odd))

print()

print(len(even))
print(len(odd))

print()
print("mississipi".count("ssi"))

even.extend(odd)
print(even)

another_even = even
print(another_even)

another_list = sorted(even)
print(another_list)

even.sort()
print(even)

even.sort(reverse=True)
print(even)
print(another_even)

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

digits = sorted("432985617")
print(digits)
digits = list("432985617")
print(digits)

more_numbers = list(numbers)
print(more_numbers)
print(numbers is more_numbers)
print(numbers == more_numbers)

more_numbers = numbers[:]
print(more_numbers)

more_numbers = numbers.copy()
print(more_numbers)

numbers = [odd, even]
print(numbers)

for number_list in numbers:
    print(number_list)

    for value in number_list:
        print(value)