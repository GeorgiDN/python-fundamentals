import re


def print_result(attacked_planets, planets_destroyed):
    result = ''
    result += f"Attacked planets: {len(attacked_planets)}\n"
    if attacked_planets:
        result += ''.join(([f"-> {planet}\n" for planet in sorted(attacked_planets)]))
    result += f"Destroyed planets: {len(planets_destroyed)}\n"
    if planets_destroyed:
        result += ''.join(([f"-> {planet}\n" for planet in sorted(planets_destroyed)]))
    return print(result)


rows = int(input())
attacked_planets = []
planets_destroyed = []

for message in range(rows):
    current_message = input()
    encrypt_pattern = r'[star]'
    decrypt_key = len(re.findall(encrypt_pattern, current_message, re.IGNORECASE))
    decrypt_message = ''
    for char in current_message:
        decrypted_char = chr(ord(char) - decrypt_key)
        decrypt_message += decrypted_char

    pattern = r'@[A-Za-z]+[^@\-!\:\>]*\:\d+[^@\-!\:\>]![AD]\![^@\-!\:\>]*\-\>\d+'
    matches = re.findall(pattern, decrypt_message)
    if matches:
        planet_name_pattern = r'@[a-zA-z]+'
        attack_pattern = r'![AD]!'
        planet_name = re.findall(planet_name_pattern, decrypt_message)[0][1:]
        attack_type = re.findall(attack_pattern, decrypt_message)[0][1]
        attacked_planets.append(planet_name) if attack_type == "A" else planets_destroyed.append(planet_name)

print_result(attacked_planets, planets_destroyed)

