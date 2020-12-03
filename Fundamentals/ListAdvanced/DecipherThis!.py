def digit_to_char(word):
    temp = ""
    for i in word:
        if not str(i).isdigit():
            break
        temp += i
    return word.replace(temp, chr(int(temp)))


def change_letter(word):
    temp = list(word)
    temp[1], temp[-1] = temp[-1], temp[1]
    return "".join(temp)


def decript_words(word):
    result = digit_to_char(word)
    result = change_letter(result)
    return result


word_to_deciph = input().split(" ")

deciph_words = [decript_words(i) for i in word_to_deciph]

print(" ".join(deciph_words))
