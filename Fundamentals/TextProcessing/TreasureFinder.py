key = [int(i) for i in input().split()]

text = input()
while text != "find":
    decrypt_msg = ""
    counter = 0
    for i in range(len(text)):
        if counter < len(key):
            decrypt_msg += chr(ord(text[i]) - key[counter])
        else:
            counter = 0
            decrypt_msg += chr(ord(text[i]) - key[counter])
        counter += 1
    found_item = decrypt_msg.split("&")[1]
    coordinates = decrypt_msg.split("<")[1][:-1]
    print(f"Found {found_item} at {coordinates}")
    text = input()