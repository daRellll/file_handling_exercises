with open("numbers.txt", "r") as number_file:
    numbers = []
    for line in number_file:
        numbers.append(int(line.strip()))