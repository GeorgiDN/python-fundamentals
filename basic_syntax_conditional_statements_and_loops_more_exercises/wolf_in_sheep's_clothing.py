animals = input()

# Разделяме входната низ на списък по ", "
queue = animals.split(', ')

if queue[-1] == 'wolf':  # Ако вълкът е най-близо до вас (на последна позиция в списъка)
    print("Please go away and stop eating my sheep")
else:
    wolf_position = queue.index('wolf')  # Намираме позицията на вълка в списъка
    sheep_number = len(queue) - wolf_position - 1  # Изчисляваме номера на овцете (бройка отзад назад)
    print(f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!")
