#https://judge.softuni.org/Contests/Practice/Index/2525#2


def take_initial_pieces_data(pieces_data_, rows_):
    for _ in range(rows_):
        piece_info = input().split("|")
        piece_, composer_, key_ = piece_info[0], piece_info[1], piece_info[2]
        pieces_data_[piece_] = [composer_, key_]
    return pieces_data_


def add_piece(pieces_data_, piece_, composer_, key_):
    if piece_ in pieces_data_:
        print(f"{piece_} is already in the collection!")
    else:
        pieces_data_[piece_] = [composer_, key_]
        print(f"{piece_} by {composer_} in {key_} added to the collection!")
    return pieces_data_


def remove_piece(pieces_data_, piece_to_remove_):
    if piece_to_remove_ not in pieces_data_:
        print(f"Invalid operation! {piece_to_remove_} does not exist in the collection.")
    else:
        del pieces_data_[piece_to_remove_]
        print(f"Successfully removed {piece_to_remove_}!")
    return pieces_data_


def change_key(pieces_data_, piece_, new_key_):
    if piece_ not in pieces_data_:
        print(f"Invalid operation! {piece_} does not exist in the collection.")
    else:
        pieces_data_[piece_].pop()
        pieces_data_[piece_].append(new_key_)
        print(f"Changed the key of {piece_} to {new_key_}!")
    return pieces_data_


def print_result(pieces_data_):
    result = ''
    for curr_piece, composer_data in pieces_data_.items():
        curr_composer, curr_key = composer_data[0], composer_data[1]
        result += f"{curr_piece} -> Composer: {curr_composer}, Key: {curr_key}\n"
    return print(result)


def main():
    pieces_data = {}
    rows = int(input())

    pieces_data = take_initial_pieces_data(pieces_data, rows)

    while True:
        data = input().split("|")
        command = data[0]

        if command == "Stop":
            break

        elif command == "Add":
            piece, composer, key = data[1], data[2], data[3]
            pieces_data = add_piece(pieces_data, piece, composer, key)

        elif command == "Remove":
            piece_to_remove = data[1]
            pieces_data = remove_piece(pieces_data, piece_to_remove)

        elif command == "ChangeKey":
            piece, new_key = data[1], data[2]
            pieces_data = change_key(pieces_data, piece, new_key)

    print_result(pieces_data)


if __name__ == "__main__":
    main()





# num_of_pieces = int(input())
# piano_pieces = {}

# for i in range(num_of_pieces):
#     curr_pieces = input().split('|')
#     piece1 = curr_pieces[0]
#     composer1 = curr_pieces[1]
#     keyy1 = curr_pieces[2]

#     if piece1 not in piano_pieces:
#         piano_pieces[piece1] = {'composer': composer1, 'key': keyy1}

# while True:
#     command = input()
#     if command == 'Stop':
#         break

#     info = command.split('|')

#     if info[0] == 'Add':
#         piece = info[1]
#         composer = info[2]
#         keyy = info[3]

#         if piece not in piano_pieces:
#             piano_pieces[piece] = {'composer': composer, 'key': keyy}
#             print(f"{piece} by {composer} in {keyy} added to the collection!")
#         else:
#             print(f"{piece} is already in the collection!")

#     elif info[0] == 'Remove':
#         piece_to_remove = info[1]

#         if piece_to_remove in piano_pieces:
#             del piano_pieces[piece_to_remove]
#             print(f"Successfully removed {piece_to_remove}!")
#         else:
#             print(f"Invalid operation! {piece_to_remove} does not exist in the collection.")

#     elif info[0] == 'ChangeKey':
#         piece_to_change = info[1]
#         new_key = info[2]

#         if piece_to_change in piano_pieces:
#             piano_pieces[piece_to_change]['key'] = new_key
#             print(f"Changed the key of {piece_to_change} to {new_key}!")
#         else:
#             print(f"Invalid operation! {piece_to_change} does not exist in the collection.")

# for piece_, data in piano_pieces.items():
#     composer_ = data['composer']
#     key_ = data['key']
#     print(f"{piece_} -> Composer: {composer_}, Key: {key_}")
