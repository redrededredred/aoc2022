def find_elf_values(filename="input.txt"):

    index = 1
    elf_values = {}
    temp_value = 0

    with open(filename, "r") as file:
        for line in file.readlines():
            if line.strip().isalnum():
                temp_value += int(line.strip())
            else:
                elf_values[index] = temp_value
                temp_value = 0
                index += 1

    return elf_values


if __name__ == "__main__":
    elf_values = find_elf_values()
    print(max(elf_values.values()))

    # part 2 here
    # bad solution
    temp = []
    for i in elf_values.values():
        temp.append(i)
    temp.sort()
    part2 = temp[-1] + temp[-2] + temp[-3]
    print(part2)

else:
    raise BaseException
