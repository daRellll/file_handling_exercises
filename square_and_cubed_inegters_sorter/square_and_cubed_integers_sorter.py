class OddAndEvenNumbersSorterAndTransformer:
    def __init__(self, integers_file):
        self.integers_file = integers_file
        self.numbers = []
        self.odd_numbers = []
        self.even_numbers = []

    def integers_file_data_loader(self):
        with open(self.integers_file) as integers_file:
            for line in integers_file:
                self.numbers.append(int(line.strip()))

    def odd_and_even_numbers_sorter(self):
        if len(self.numbers) == 20:
            print(f"\033[92mConfirmed! \033[0m{len(self.numbers)} numbers are in the file, now sorting...")
            for number in self.numbers:
                if number % 2 == 0:
                    self.even_numbers.append(number)
                else:
                    self.odd_numbers.append(number)
        elif len(self.numbers) > 20:
            print(
                f"\033[91mError! \033[0m{len(self.numbers)} numbers is too much! Delete some lines in numbers.txt file to continue")
        else:
            print(
                f"\033[91mError! \033[0m{len(self.numbers)} numbers is too little! Add more numbers in numbers.txt file to continue")
