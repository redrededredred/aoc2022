
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
                    print(ord(char) - 96)
                    print(char)
                    break
                else:
                    priority_sum += ord(char) - 38
                    print(ord(char) - 38)
                    print(char)
                    break

    return priority_sum

def p2(data)
if __name__ == "__main__":
    bag_number = 1
    data = {}
    with open("input.txt", "r") as file:
        for line in file.readlines():
            data[bag_number] = line.strip()
            bag_number += 1
    print(p1(data))
else:
    raise BaseException