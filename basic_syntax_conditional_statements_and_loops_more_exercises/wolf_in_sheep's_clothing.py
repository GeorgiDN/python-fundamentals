queue = input().split(', ')

if queue[-1] == 'wolf':
    print("Please go away and stop eating my sheep")
else:
    wolf_position = queue.index('wolf')
    sheep_number = len(queue) - wolf_position - 1
    print(f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!")


# queue = input().split(', ')
# print("Please go away and stop eating my sheep") if queue[-1] == 'wolf' else print(f"Oi! Sheep number {len(queue) - queue.index('wolf') - 1}! You are about to be eaten by a wolf!")


