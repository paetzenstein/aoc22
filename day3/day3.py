import string
if __name__=="__main__":
    f = open("input_day3", "r")
    lines = f.readlines()

    alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    sum = 0
    i = 0

    while i < len(lines):
        elf_1 = set((lines[i].strip()))
        elf_2 = set(lines[i+1].strip())
        elf_3 = set(lines[i+2].strip())
        i += 3
        common_c = elf_1 & elf_2 & elf_3
        print(list(common_c).pop())
        sum += alphabet.index(list(common_c).pop()) + 1

    print(sum)





