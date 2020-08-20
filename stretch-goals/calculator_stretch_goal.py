def calculator(a, b, operator):
    switcher = {
        '+': a+b,
        '-': a-b,
        '/': (int)(a/b),
        '*': a*b,
    }
    temp = switcher.get(operator, "Something Wrong")
    result = []

    while temp > 2:
        result.append((int)(temp % 2))
        temp = temp/2
    result.append((int)(temp))
    return int(''.join(["%d" % x for x in result.__reversed__()]))


print(calculator(2, 4, "+"))  # Should print 110 to the console
print(calculator(10, 3, "-"))  # Should print 111 to the console
print(calculator(4, 7, "*"))  # Should output 11100 to the console
print(calculator(100, 2, "/"))  # Should print 110010 to the console
