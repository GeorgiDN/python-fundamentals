def generate_loading_bar(percentage):
    loading = f"{percentage}% [{'%' * (percentage // 10)}{'.' * (10 - (percentage // 10))}]"

    if percentage < 100:
        loading += "\nStill loading..."
    else:
        loading = "100% Complete!\n[%%%%%%%%%%]"

    return loading



number = int(input())
loading_bar = generate_loading_bar(number)
print(loading_bar)
