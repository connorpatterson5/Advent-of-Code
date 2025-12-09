def process_lines(input):
    zero_count = 0
    current_position = 50

    for rotation in input:
        direction = rotation[0]
        steps = int(rotation[1:])
        if direction == 'R':
            current_position = (current_position + steps) % 100
        elif direction == 'L':
            current_position = (current_position - steps) % 100
        if current_position == 0:
            zero_count += 1
    return zero_count


if __name__ == '__main__':
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')

    result = process_lines(lines)
    print(f"Result: {result}")