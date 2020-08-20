#submitted by Md Abu Joni
def calculator(a, b, operator):
    switcher = {
        '+': a+b,
        '-': a-b,
        '/': int(a/b),
        '*': a*b,
    }
    return switcher.get(operator, "Something Wrong")


print(calculator(2, 4, "+"))  # Should print 6 to the console
print(calculator(10, 3, "-"))  # Should print 7 to the console
print(calculator(4, 7, "*"))  # Should print 28 to the console
print(calculator(100, 2, "/"))  # Should print 50 to the console
