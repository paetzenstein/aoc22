
## Rock A(elf); X(me); Score = 1
## Paper B(elf) Y(me); Score = 2
## Scissor C(elf) Z(me); Score = 3
## Win = 6; Draw = 3; Lose = 0
if __name__=="__main__":
    f = open("input_day2","r")
    lines = f.readlines()
    score = 0
    def game(elf_input, my_input):
        if (elf_input == "A"):
            if (my_input == "X"):
                return 4
            elif (my_input == "Y"):
                return 8
            elif (my_input == "Z"):
                return 3
            else:
                print("invalid input")
        if (elf_input == "B"):
            if (my_input == "X"):
                return 1
            elif (my_input == "Y"):
                return 5
            elif (my_input == "Z"):
                return 9
            else:
                print("invalid input")
        if (elf_input == "C"):
            if (my_input == "X"):
                return 7
            elif (my_input == "Y"):
                return 2
            elif (my_input == "Z"):
                return 6
            else:
                print("invalid input")
        else:
            print("invalid input")

    for line in lines:
        line = line.strip()
        values = line.split()
        score += game(values[0], values[1])
    print(score)
