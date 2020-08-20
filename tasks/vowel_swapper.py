#submitted by Md Abu Joni
def vowel_swapper(string):
    dict = {'a': 4, 'e': 3, 'i': '!', 'o': "ooo", 'O': "000", 'u': "|_|"}
    arr_char = list(string)
    result_str = ""
    for charc in arr_char:
        if charc != 'O':
            if charc.lower() in dict:
                result_str += (str)(dict[charc.lower()])
            else:
                result_str += charc
        else:
            result_str += (str)(dict[charc])

    return result_str


print(vowel_swapper("aA eE iI oO uU"))  # Should print "44 33 !! ooo000 |_||_|" to the console
print(vowel_swapper("Hello World"))  # Should print "H3llooo Wooorld" to the console
# Should print "3v3ryth!ng's 4v4!l4bl3" to the console
print(vowel_swapper("Everything's Available"))
