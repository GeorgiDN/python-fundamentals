#https://judge.softuni.org/Contests/Practice/Index/2525#2

num_of_pieces = int(input())
piano_pieces = {}

for i in range(num_of_pieces):
    curr_pieces = input().split('|')
    piece1 = curr_pieces[0]
    composer1 = curr_pieces[1]
    keyy1 = curr_pieces[2]

    if piece1 not in piano_pieces:
        piano_pieces[piece1] = {'composer': composer1, 'key': keyy1}

while True:
    command = input()
    if command == 'Stop':
        break

    info = command.split('|')

    if info[0] == 'Add':
        piece = info[1]
        composer = info[2]
        keyy = info[3]

        if piece not in piano_pieces:
            piano_pieces[piece] = {'composer': composer, 'key': keyy}
            print(f"{piece} by {composer} in {keyy} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif info[0] == 'Remove':
        piece_to_remove = info[1]

        if piece_to_remove in piano_pieces:
            del piano_pieces[piece_to_remove]
            print(f"Successfully removed {piece_to_remove}!")
        else:
            print(f"Invalid operation! {piece_to_remove} does not exist in the collection.")

    elif info[0] == 'ChangeKey':
        piece_to_change = info[1]
        new_key = info[2]

        if piece_to_change in piano_pieces:
            piano_pieces[piece_to_change]['key'] = new_key
            print(f"Changed the key of {piece_to_change} to {new_key}!")
        else:
            print(f"Invalid operation! {piece_to_change} does not exist in the collection.")

for piece_, data in piano_pieces.items():
    composer_ = data['composer']
    key_ = data['key']
    print(f"{piece_} -> Composer: {composer_}, Key: {key_}")
