def transform_strings(str1, str2):
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            str1 = str1[:i] + str2[i] + str1[i + 1:]
            print(str1)

str1 = input()
str2 = input()

transform_strings(str1, str2)
