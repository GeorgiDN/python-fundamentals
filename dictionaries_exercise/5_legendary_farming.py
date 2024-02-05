def legendary_farming():
    key_materials = {"shards": 0, "fragments": 0, "motes": 0}
    junk_items = {}
    while max(key_materials.values()) < 250:
        items_list = input().lower().split()
        for index, element in enumerate(items_list):
            if index % 2 != 0:
                material = element
                quantity = int(items_list[index - 1])
                if element.lower() not in key_materials:
                    if element.lower() not in junk_items:
                        junk_items[material] = 0
                    junk_items[material] += quantity
                else:
                    key_materials[material] += quantity
                    if key_materials[element] >= 250:
                        if element == "shards":
                            print("Shadowmourne obtained!")
                        elif element == "fragments":
                            print("Valanyr obtained!")
                        elif element == "motes":
                            print("Dragonwrath obtained!")
                        break

    win_element = max(key_materials, key=key_materials.get)
    key_materials[win_element] -= 250

    print('\n'.join([f"{mat}: {qty}" for mat, qty in key_materials.items()]))
    print('\n'.join([f"{mat}: {qty}" for mat, qty in junk_items.items()]))


legendary_farming()
