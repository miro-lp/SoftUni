def data_type(word):
    result = None
    if str(word).isdigit():
        result = int(word) * 2
    elif str(word).isalpha():
        result = "$" + word + "$"
    else:
        result = round(float(word) * 1.5, 2)
    return result

word = input()

print(data_type(word))

