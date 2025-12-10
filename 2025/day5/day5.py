def process_lines(lines):
    result = 0

    # part 1 answer:
    '''
    ingredient_indicator = -1
    for i in range(len(lines)):
        if lines[i] == '':
            ingredient_indicator = i
            break
    
    for j in range(ingredient_indicator + 1, len(lines)):
        available_ingredient_id = int(lines[j])
        for k in range(0, ingredient_indicator):
            ingredient_id_min, ingredient_id_max = lines[k].split('-')
            if int(ingredient_id_min) <= available_ingredient_id <= int(ingredient_id_max):
                result += 1
                break
    '''

    # part 2 answer: needed chatGPT help
    ranges = []
    for line in lines:
        if line == "":
            break
        low, high = map(int, line.split("-"))
        ranges.append((low, high))

    ranges.sort()
    merged_ranges = []
    current_start, current_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            merged_ranges.append((current_start, current_end))
            current_start, current_end = start, end

    merged_ranges.append((current_start, current_end))

    result = sum(end - start + 1 for start, end in merged_ranges)
    return result


if __name__ == '__main__':
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines()]
    result = process_lines(lines)
    print(f"Result: {result}\n")
