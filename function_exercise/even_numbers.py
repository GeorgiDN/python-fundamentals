number_list = list(map(int, input().split()))

def list_even():
    even_list = []

    for num in number_list:
        if num % 2 == 0:
            even_list.append(num)
    print(even_list)

list_even()
