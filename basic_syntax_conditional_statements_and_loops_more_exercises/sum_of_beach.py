input_string = input()

input_string = input_string.lower()

sand_count = input_string.count("sand")
water_count = input_string.count("water")
fish_count = input_string.count("fish")
sun_count = input_string.count("sun")


total_count = sand_count + water_count + fish_count + sun_count

print(total_count)
