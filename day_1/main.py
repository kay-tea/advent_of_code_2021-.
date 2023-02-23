# day 1

def selection():
    data = read_file()
    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data, 3)}")
    
def read_file():
    with open('data.txt') as f:
        data = [int(i) for i in f]
    return data

# part 1: count the number of times A NUMBER increases from the previous

def part_one(data):
    count = 0
    x = data[0]

    for i in data:
        if i > x:
            count +=1 
        x = i

    return count

# part 2: count the number of times the sum of measurements in a SECTION OF NUMBERS (3)
# increases from the previous

def part_two(data, section_size):
    prev_data_sum = sum(data[0:section_size])
    count = 0

    for i in range(1, len(data) - (section_size-1)):
        data_sum = sum(data[i:i + section_size])
        
        if data_sum > prev_data_sum:
            count += 1
        prev_data_sum = data_sum
    
    return count

if __name__ == '__main__':
    selection()
