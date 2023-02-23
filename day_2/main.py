# day 2

def selection():
    data = read_file()
    print(f'Part One: {part_one(data)}')
    print(f'Part Two: {part_two(data)}')

def read_file():
    data = [i.strip().split(' ') for i in open('data.txt', 'r').readlines()]
    return data

# part 1: find the result of multiplying the final horizontal number by the 
#   final depth

def part_one(data):
    horizonal, depth = 0, 0
    for i in data:
        if i[0] == 'forward':
            horizonal += int(i[1])
        elif i[0] == 'down':
            depth += int(i[1])
        else:
            depth -= int(i[1])
    return horizonal * depth

# part 2: with aim now added, calculate the result of the final 
#    horizontal position and depth

def part_two(data):
    horizontal, depth, aim = 0, 0, 0
    for i in data:
        if i[0] == 'forward':
            horizontal += int(i[1])
            depth += (aim * int(i[1]))
        elif i[0] == 'down':
            aim += int(i[1])
        else:
            aim -= int(i[1])
    return horizontal * depth

if __name__ == '__main__':
    selection()
