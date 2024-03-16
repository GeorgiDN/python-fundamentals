import re


def calculate_health(demons_list):
    demons_data_ = {}
    health_pattern = r'[^\d\+\-\*\/\.\s]'
    for demon in demons_list:
        health = 0
        matches = re.findall(health_pattern, demon)
        for char in matches:
            health += ord(char)
        demons_data_[demon] = []
        demons_data_[demon].append(health)
    return demons_data_


def calculate_damage(demons_data_, demons_list):
    damage_pattern = r"\-*\d+(\.\d+)*"
    for demon in demons_list:
        damage_match = re.finditer(damage_pattern, demon)
        damage = sum([float(x.group()) for x in damage_match])
        for ch in demon:
            if ch == '*':
                damage *= 2
            elif ch == '/':
                damage /= 2

        demons_data_[demon].append(damage)
    return demons_data_


def print_result(demons_data_):
    result = ''
    for demon_name, info in demons_data_.items():
        demon_health, demon_damage = info[0], info[1]
        result += f"{demon_name} - {demon_health} health, {demon_damage:.2f} damage\n"

    return print(result)


def main():
    input_data = sorted([x.strip() for x in input().split(",")])
    demons_data = calculate_health(input_data)
    demons_data = calculate_damage(demons_data, input_data)
    print_result(demons_data)


if __name__ == '__main__':
    main()
