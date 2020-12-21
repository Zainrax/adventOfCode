if __name__ == "__main__":
    f = open("./input.txt")
    target = 2020
    lines = f.readlines()
    lines = [int(i) for i in lines]
    initial_table = {}
    inTable = []
    for idx, initial_num in enumerate(lines):
        table = {}
        possible = target - initial_num
        lines.pop(idx)
        arr = lines.copy()
        arr.pop(idx)
        for num in arr:
            if num in table:
                inTable.append(num * table[num] * initial_num)
                continue
            num_pair = possible - num
            table[num_pair] = num

    print(inTable)

