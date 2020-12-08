text = input()

repeat_text = ""
non_digit_text = ""
uniq_sym_count = 0
last_sym = ""

for i in range(len(text)):
    if not text[i].isdigit():
        non_digit_text += text[i]
    else:
        if i <= (len(text)-2) and text[i + 1].isdigit():
            rep_num = int(text[i] + text[i + 1])
            repeat_text += non_digit_text.upper() * rep_num
            non_digit_text = ""
        else:
            repeat_text += non_digit_text.upper() * int(text[i])
            non_digit_text = ""

for i in repeat_text:
    if i not in last_sym:
        last_sym+=i
        uniq_sym_count+=1
print(f"Unique symbols used: {uniq_sym_count}")
print(repeat_text)
