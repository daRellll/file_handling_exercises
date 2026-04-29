with open("numbers.txt", "r") as number_file:
    numbers = []
    for line in number_file:
        numbers.append(int(line.strip()))

odd_numbers = []
even_numbers = []

if len(numbers) == 20:
    print(f"Confirmed! {len(numbers)} are in the file, now sorting...")
elif len(numbers) > 20:
    print(f"Error! {len(numbers)} is too much! Delete some lines in numbers.txt file to continue")
else:
    print(f"Error! {len(numbers)} is too little! Add more numbers in numbers.txt file to continue")

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

with open("odd.txt", "w") as odd_number_file:
    for number in odd_numbers:
        odd_number_file.write(f"{number}\n")
with open("even.txt", "w") as even_number_file:
    for number in even_numbers:
        even_number_file.write(f"{number}\n")