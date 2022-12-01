def find_most_valuable_elf(filename="input.txt"):

    index = 1
    elf_values = {}
    temp_value = 0

    with open(filename, "r") as file:
        for line in file.readlines():
            if line.strip().isalnum():
                print(line.strip())
                temp_value += int(line.strip())
            else:
                elf_values[index] = temp_value
                temp_value = 0
                index += 1

    return max(elf_values.values())


if __name__ == "__main__":
    print(find_most_valuable_elf())
else:
    raise BaseException
