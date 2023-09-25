cards = input().split()
faro_count = int(input())

half_size = len(cards) // 2

for _ in range(faro_count):
    first_half = cards[:half_size]
    second_half = cards[half_size:]
    shuffled_deck = []

    for i in range(half_size):
        shuffled_deck.append(first_half[i])
        shuffled_deck.append(second_half[i])

    cards = shuffled_deck

print(cards)
