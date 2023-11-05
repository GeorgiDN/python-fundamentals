text_list = list(text)

check_symbols = []

for ch in text_list:
    if ch not in check_symbols:
        check_symbols.append(ch)
    if check_symbols[-1] != ch:
        check_symbols.append(ch)

print(''.join(check_symbols))
