with open("numbers.txt", "r") as number_file:
    numbers = []
    for line in number_file:
        numbers.append(int(line.strip()))

if len(numbers) == 20:
    print(f"Confirmed! {len(numbers)} are in the file, now sorting...")
elif len(numbers) < 20:
    print(f"Error! {len(numbers)} is too much! Delete some lines in numbers.txt file to continue")
else:
    print(f"Error! {len(numbers)} is too little! Add more numbers in numbers.txt file to continue")

