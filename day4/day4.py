def get_number(i, j):
    if i == j:
        return [i]
    numbers = []
    for x in range(i, j + 1):
        numbers.append(x)
    return numbers


def part1():
    f = open("input_day4", "r")
    lines = f.readlines()
    sum = 0
    for line in lines:
        line = line.strip()
        line = line.split(',')
        elf_1 = line[0].split('-')
        elf_2 = line[1].split('-')
        elf_1_numbers = get_number(int(elf_1[0]), int(elf_1[1]))
        elf_2_numbers = get_number(int(elf_2[0]), int(elf_2[1]))
        elf_1_numbers = set(elf_1_numbers)
        elf_2_numbers = set(elf_2_numbers)
        compare = set(elf_1_numbers & elf_2_numbers)
        if compare == elf_1_numbers or compare == elf_2_numbers:
            sum += 1
    print('In ' + str(sum) + ' assignment pairs one range does fully contain the other!')


def part2():
    f = open("input_day4", "r")
    lines = f.readlines()
    sum = 0
    for line in lines:
        line = line.strip()
        line = line.split(',')
        elf_1 = line[0].split('-')
        elf_2 = line[1].split('-')
        elf_1_numbers = get_number(int(elf_1[0]), int(elf_1[1]))
        elf_2_numbers = get_number(int(elf_2[0]), int(elf_2[1]))
        elf_1_numbers = set(elf_1_numbers)
        elf_2_numbers = set(elf_2_numbers)
        compare = set(elf_1_numbers & elf_2_numbers)
        if compare:
            sum += 1
    print('In ' + str(sum) + ' assignment pairs the range does overlap!')


if __name__=="__main__":
    part1()
    part2()
