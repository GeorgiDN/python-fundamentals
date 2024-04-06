import math

number_biscuits_per_day = int(input())
workers = int(input())

biscuits_competing_factory = int(input())

total_production = 0

for day in range(1, 31):
    production_per_day = number_biscuits_per_day * workers
    if day % 3 == 0:
        production_per_day *= 0.75
        production_per_day = math.floor(production_per_day)
    total_production += production_per_day

diff = abs(total_production - biscuits_competing_factory)
percent_diff = (diff / biscuits_competing_factory) * 100
print(f"You have produced {total_production} biscuits for the past month.")

if total_production > biscuits_competing_factory:
    print(f"You produce {percent_diff:.2f} percent more biscuits.")
else:
    print(f"You produce {percent_diff:.2f} percent less biscuits.")
  
