
def p1(data):
    # A for Rock, B for Paper, C for Scissors
    # X for Rock, Y for Paper, Z for Scissors
    # 1p for Rock, 2p Paper, 3p for Scissors, 0p lost, 3p draw, 6p win

    score = 0
    for game in data.values():
        player = game.split(" ")[1]
        enemy = game.split(" ")[0]

        if player == "X":
            score += 1
            if enemy == "A":
                score += 3
            elif enemy == "C":
                score += 6
        elif player == "Y":
            score += 2
            if enemy == "A":
                score += 6
            elif enemy == "B":
                score += 3
        else:
            score += 3
            if enemy == "B":
                score += 6
            elif enemy == "C":
                score += 3

    return score


def p2(data):
    # X lose, Y draw, Z win

    score = 0
    for game in data.values():
        option = game.split(" ")[1]
        enemy = game.split(" ")[0]

        if enemy == "A":
            if option == "X":
                score += 3
            elif option == "Y":
                score += 4
            else:
                score += 8
        elif enemy == "B":
            if option == "X":
                score += 1
            elif option == "Y":
                score += 5
            else:
                score += 9
        else:
            if option == "X":
                score += 2
            elif option == "Y":
                score += 6
            else:
                score += 7

    return score


if __name__ == "__main__":
    current_round = 1
    data = {}
    with open("input.txt", "r") as file:
        for line in file.readlines():
            data[current_round] = line.strip()
            current_round += 1
    print(p2(data))
else:
    raise BaseException

