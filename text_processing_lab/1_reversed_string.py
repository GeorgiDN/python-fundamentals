text = input()

while text != 'end':
    text_reversed = text[::-1]
    print(f"{text} = {text_reversed}")
    text = input()




# text = input()
# while text != 'end':
#     text_reversed = ''
#     for ch in reversed(text):
#         text_reversed += ch
#     print(text + " = " + text_reversed)
#     text = input()
