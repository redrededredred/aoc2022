def p1(data):
    matches = 0
    for i in data.values():

        l1 = [int(section) for section in i[0].split('-')]
        l2 = [int(section) for section in i[1].split('-')]

        if l1[0] >= l2[0] and l1[1] <= l2[1] or l2[0] >= l1[0] and l2[1] <= l1[1]:
            matches += 1
    return matches


def p2(data):
    matches = 0
    for i in data.values():

        l1 = [int(section) for section in i[0].split('-')]
        l2 = [int(section) for section in i[1].split('-')]

        if l1[0] <= l2[0] <= l1[1] or l2[0] <= l1[0] <= l2[1]:
            matches += 1
    return matches


if __name__ == "__main__":
    index = 1
    data = {}
    with open("input.txt", "r") as file:
        for line in file.readlines():
            data[index] = line.strip().split(sep=",")
            index += 1

    print(p1(data))
    print(p2(data))

else:
    raise BaseException