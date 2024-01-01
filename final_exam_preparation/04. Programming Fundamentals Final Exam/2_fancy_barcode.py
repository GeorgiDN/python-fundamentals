import re

barcode_count = int(input())
validation_pattern = r"^@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+$"
for _ in range(barcode_count):
    barcode = input()
    validation = re.findall(validation_pattern, barcode)
    validation = ''.join(validation)
    if validation:
        code_pattern = r"\d+"
        match = re.findall(code_pattern, validation)
        if match:
            product_group = "".join(match)
        else:
            product_group = "00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")
      
