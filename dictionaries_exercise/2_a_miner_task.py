def fill_the_dictionary(resource_, qnty, res_with_quantity):
    if resource_ not in res_with_quantity:
        res_with_quantity[resource_] = 0
    res_with_quantity[resource_] += qnty
    return res_with_quantity


def miner_task():
    resources_with_quantity = {}
    while True:
        curr_resource = input()
        if curr_resource == "stop":
            break
        quantity = int(input())
        resources_with_quantity = fill_the_dictionary(curr_resource, quantity, resources_with_quantity)

    result = '\n'.join([f"{res} -> {qty}" for res, qty in resources_with_quantity.items()])
    return print(result)


miner_task()



# command = input()
# my_dictionary = {}

# while command != 'stop':
#     quantity = int(input())
#     key = command
#     value = quantity

#     if key not in my_dictionary:
#         my_dictionary[key] = int(value)
#     else:
#         my_dictionary[key] += int(value)

#     command = input()

# for key, value in my_dictionary.items():
#     print(f"{key} -> {value}")
  
