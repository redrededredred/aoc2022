
def p1(data):
    priority_sum = 0
    for i in data.values():
        part_1 = i[:len(i) // 2]
        part_2 = i[len(i) // 2:]
        print(f"Part 1: {part_1}")
        print(f"Part 2: {part_2}")
        for char in part_1:
            if char in part_2:
                if char.islower():
                    priority_sum += ord(char) - 96
                    break
                else:
                    priority_sum += ord(char) - 38
                    break

    return priority_sum


def p2(data):
    priority_sum = 0
    only_data = []
    for i in data.values():
        only_data.append(i)
    for i in range(0, len(only_data), 3):
        group = only_data[i:i+3]
        bag1 = group[0]
        bag2 = group[1]
        bag3 = group[2]

        for char in bag1:
            if char in bag2 and char in bag3:
                if char.islower():
                    priority_sum += ord(char) - 96
                    break
                else:
                    priority_sum += ord(char) - 38
                    break

    return priority_sum


if __name__ == "__main__":
    bag_number = 1
    data = {}
    with open("input.txt", "r") as file:
        for line in file.readlines():
            data[bag_number] = line.strip()
            bag_number += 1
    print(p2(data))

else:
    raise BaseException