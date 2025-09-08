def sum_eo():
    n = int(input("Please enter a positive number: "))
    t = input("Please enter on of the letters 'e', 'o': ")
    if t == "e":
        num = []
        for i in range(1, n):
            if i % 2 == 0:
                num.append(i)
        total = sum(num)
        return total
    elif t == "o":
        num = []
        for i in range(1, n):
            if i % 2 != 0:
                num.append(i)
        total = sum(num)
        return total
    else:
        total = -1
        return total
    
print(sum_eo())

# def sum_eo(n, t):
#     if t == "e":
#         start = 2
#     elif t == 'o':
#         start = 1
#     else:
#         return -1

#     return sum(range(start, n, 2))


# x = sum_eo(11, 'e')
# print(x)