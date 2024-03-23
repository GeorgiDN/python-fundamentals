import re

barcodes_count = int(input())
pattern = r'(@[#]+)([A-Z][a-zA-Z0-9]{4,}[A-Z])(@[#]+)'

for _ in range(barcodes_count):
    barcode = input()
    matches = re.findall(pattern, barcode)
    if matches:
        code_pattern = r'\d+'
        digits_matches = re.findall(code_pattern, barcode)
        if digits_matches:
            product_group = ''.join(digits_matches)
        else:
            product_group = '00'
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")


# import re

# barcodes_count = int(input())
# product_group = {}

# for _ in range(barcodes_count):
#     info = input()
#     pattern = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+$"
#     matches = re.findall(pattern, info)

#     if not matches:
#         print("Invalid barcode")
#     else:
#         for match in matches:
#             name = match

#             digits = [char for char in name if char.isdigit()]
#             if not digits:
#                 product_group[name] = "00"
#             else:
#                 product_group[name] = ''.join(digits)

#             print(f"Product group: {product_group[name]}")

