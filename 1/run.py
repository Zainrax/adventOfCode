if __name__ == "__main__":
    f = open("./input.txt")
    target = 2020
    lines = f.readlines()
    lines = [int(i) for i in lines]
    table = {}
    inTable = []
    for num in lines:
        if num in table:
            inTable.append(num * table[num])
            continue
        num_pair = target - num
        table[num_pair] = num

    print(inTable)

