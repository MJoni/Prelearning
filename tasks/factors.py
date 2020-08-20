#submitted by Md Abu Joni
def factors(number):
    result = []
    for index in range(2, number-1):
        if (number % index) == 0:
            result.append(index)
    return result


print(factors(15))  # Should print [3, 5] to the console
print(factors(12))  # Should print [2, 3, 4, 6] to the console
print(factors(13))  # Should print “[]” (an empty list) to the console
