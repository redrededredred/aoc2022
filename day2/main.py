
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
    

if __name__ == "__main__":
    current_round = 1
    data = {}
    with open("input.txt", "r") as file:
        for line in file.readlines():
            data[current_round] = line.strip()
            current_round += 1
    print(p1(data))
else:
    raise BaseException

