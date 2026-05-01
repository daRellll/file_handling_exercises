class OddAndEvenNumbersSorter:
    def __init__(self, numbers_file):
        self.numbers_file = numbers_file
        self.numbers = []
        self.odd_numbers = []
        self.even_numbers = []

    def numbers_file_data_loader(self):
        with open(self.numbers_file, "r") as number_file:
            for line in number_file:
                self.numbers.append(int(line.strip()))

if len(numbers) == 20:
    print(f"\033[92mConfirmed! \033[0m{len(numbers)} numbers are in the file, now sorting...")
elif len(numbers) > 20:
    print(f"\033[91mError! \033[0m{len(numbers)} numbers is too much! Delete some lines in numbers.txt file to continue")
else:
    print(f"\033[91mError! \033[0m{len(numbers)} numbers is too little! Add more numbers in numbers.txt file to continue")

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