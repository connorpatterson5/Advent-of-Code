def process_lines(lines):
    invalid_id_count = 0

    for product in lines:
        id1, id2 = map(int, product.split('-'))

        for num in range(id1, id2 + 1):
            str_num = str(num)
            length = len(str_num)


            # part 1 answer:
            '''
            for num in range(id1, id2 + 1): 
                if len(length) % 2 != 0: 
                    continue 
                str_num = str(num) 
                half = int(length / 2) 
                if str_num[:half] == str_num[half:]: 
                    invalid_id_count += int(str_num)
            '''

            # part 2 answer:
            invalid = False
            for l in range(1, length // 2 + 1):
                if length % l != 0:
                    continue

                seq = str_num[:l]
                repeats = length // l

                if seq * repeats == str_num:
                    invalid = True
                    break

            if invalid:
                invalid_id_count += num

    return invalid_id_count


if __name__ == '__main__':
    with open("input.txt", "r", encoding="utf-8") as f:
        line = f.read().strip()

    inputs = line.split(',')
    result = process_lines(inputs)
    print(f"Result: {result}")
