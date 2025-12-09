def process_lines(lines):
    total_joltage = 0
    for line in lines:

        # part 1 answer:
        '''
        max_joltage = 0
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                joltage_pair = int(line[i] + line[j])
                if joltage_pair > max_joltage:
                    max_joltage = joltage_pair
        '''

        # part 2 answer:
        for i in range(len(line)):
            max_joltage = ''
            pos = 0
            for _ in range(12):
                end = len(line) - (12 - len(max_joltage)) + 1
                slice_to_check = line[pos:end]
                max_digit = max(slice_to_check)
                max_index = slice_to_check.index(max_digit)
                max_joltage += max_digit
                pos += max_index + 1

        total_joltage += int(max_joltage)
    return total_joltage


if __name__ == '__main__':
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    result = process_lines(lines)
    print(f"Result: {result}")
