def vowel_swapper(string):
    dict = {'a': 4, 'e': 3, 'i': '!', 'o': "ooo", 'O': "000", 'u': "|_|"}
    arr_char = list(string)
    index = ""

    for i in range(0, len(arr_char)-1):
        char_holder = arr_char[i]
        if char_holder != 'O':
            if char_holder.lower() in dict:
                index = char_holder.lower()
                for j in range(i+1, len(arr_char)):
                    if arr_char[j].lower() == index and arr_char[j] != 'O':
                        arr_char[j] = (str)(dict[index])
                        index = ""
                        break
                    if arr_char[j] == 'O' and index.upper() == arr_char[j]:
                        arr_char[j] = dict['O']
                        index = ""
                        break
            else:
                arr_char[i] = char_holder
        else:
            index = char_holder
            for j in range(i+1, len(arr_char)):
                if arr_char[j].lower() == index.lower():
                    arr_char[j] = (str)(dict[arr_char[j]])
                    index = ""
                    break

    return "".join(arr_char)


# Should print "a/\a e3e i!i o000o u\/u" to the console
print(vowel_swapper("aAa eEe iIi oOo uUu"))
print(vowel_swapper("Hello World"))  # Should print "Hello Wooorld" to the console
# Should print "Ev3rything's Av/\!lable" to the console
print(vowel_swapper("Everything's Available"))
