
"""
Rock: 1
Paper: 2
Scissors: 3

Lose: 0     // X
Draw: 3     // Y
Win: 6      // Z
"""
if __name__=="__main__":
    f = open("input_day2","r")
    lines = f.readlines()
    score = 0
    def game(elf_input, my_input):
        if (my_input == "X"):
            if (elf_input == "A"):
                return 3
            elif (elf_input == "B"):
                return 1
            elif (elf_input == "C"):
                return 2
            else:
                print("invalid input_day3")
        if (my_input == "Y"):
            if (elf_input == "A"):
                return 4
            elif (elf_input == "B"):
                return 5
            elif (elf_input == "C"):
                return 6
            else:
                print("invalid input_day3")
        if (my_input == "Z"):
            if (elf_input == "A"):
                return 8
            elif (elf_input == "B"):
                return 9
            elif (elf_input == "C"):
                return 7
            else:
                print("invalid input_day3")
        else:
            print("invalid input_day3")

    for line in lines:
        line = line.strip()
        values = line.split()
        score += game(values[0], values[1])
    print(score)
