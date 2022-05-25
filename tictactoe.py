characters = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"],
]
top_bottom = "---------"


def grid_base():
    print(top_bottom)
    print("|", " ".join(characters[0]), "|")
    print("|", " ".join(characters[1]), "|")
    print("|", " ".join(characters[2]), "|")
    print(top_bottom)


one_player_won = False
is_empty = True
moves = 0
grid_copy = []
winner = ""


grid_base()

while moves < 9 and not one_player_won:
    try:
        raw, column = input("Enter the coordinates: ").split()
        raw = int(raw) - 1
        column = int(column) - 1
        if characters[raw][column] != "_":
            is_empty = False
            print("This cell is occupied! Choose another one!")
            continue
        else:
            if moves % 2 == 0:
                characters[raw][column] = "X"
            else:
                characters[raw][column] = "O"
    except ValueError:
        print("You should enter numbers!")
    except IndexError:
        print("Coordinates should be from 1 to 3!")
    else:
        grid_base()
        grid_copy = [number for nests in characters for number in nests]
        options = [grid_copy[:3], grid_copy[3:6], grid_copy[6:9], grid_copy[:7:3], grid_copy[1:8:3], grid_copy[2:9:3], grid_copy[:9:4], grid_copy[2:7:2]]
        for i in options:
            if i == ["X", "X", "X"]:
                one_player_won = True
                print("X wins")
            elif i == ["O", "O", "O"]:
                one_player_won = True
                print("O wins")
        moves += 1
        if moves == 9 and not one_player_won:
                print("Draw")
                break
