import string
def read_crates():
    f = open("input_day5", "r")
    alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    lines = f.readlines()
    x = 0
    while x < 8:
        line = lines[x]
        print('Length of line:')
        print(len(line))
        for c in line:
            if c in alphabet:
                print('index of match: ')
                print(line.index(c))
        print('------------')
        x += 1



def part1():
    f = open("input_day4", "r")
    lines = f.readlines()
    sum = 0




def part2():
    f = open("input_day4", "r")
    lines = f.readlines()
    sum = 0
if __name__=="__main__":
    read_crates()
