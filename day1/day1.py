f = open("input_day1","r")
lines = f.readlines()


if __name__=="__main__":
    cur_elf = 0
    top3 = [0,0,0]
    top3_calories = 0

    def calc_top3():
        global top3_calories
        for c in top3:
            top3_calories += c
        return top3_calories

    def top3_sorter(value):
        ## define 3rd
        if (value > top3[0] and value < top3[1]):
            top3[0] = value
        ## define 2nd
        if (value > top3[1] and value < top3[2]):
            top3[0] = top3[1]
            top3[1] = value
        ## define 1st
        if (value > top3[2]):
            top3[0] = top3[1]
            top3[1] = top3[2]
            top3[2] = value


    for line in lines:
        line = line.strip()
        if (line.isdigit()):
            line = int(line)
            cur_elf += line
        else: 
            if(cur_elf > top3[0]):
                top3_sorter(cur_elf)
            cur_elf = 0
    print(calc_top3())

