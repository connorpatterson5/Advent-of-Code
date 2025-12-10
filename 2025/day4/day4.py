def process_lines(lines):
    result = 0

    while True:
        store_pos = []

        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] != '@':
                    continue
                
                # part 1 answer
                count = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < len(lines) and 0 <= nj < len(lines[i]):
                            if lines[ni][nj] == '@':
                                count += 1
                
                # part 2 answer
                if count < 4:
                    store_pos.append((i, j))

        if not store_pos:
            break

        for i, j in store_pos:
            lines[i][j] = 'x'
        result += len(store_pos)
    return result


if __name__ == '__main__':
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = [list(line.strip()) for line in f.readlines()]
    result = process_lines(lines)
    print(f"Result: {result}\n")
    print("Final state:\n")
    for line in lines:
        print(''.join(line))
