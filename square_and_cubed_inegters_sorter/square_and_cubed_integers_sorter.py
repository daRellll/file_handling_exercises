class OddAndEvenNumbersSorterAndTransformer:
    def __init__(self, integers_file):
        self.integers_file = integers_file
        self.integers = []
        self.odd_integers = []
        self.even_integers = []

    def integers_file_data_loader(self):
        with open(self.integers_file) as integers_file:
            for line in integers_file:
                self.integers.append(int(line.strip()))

    def odd_and_even_numbers_sorter(self):
        if len(self.integers) == 20:
            print(f"\033[92mConfirmed! \033[0m{len(self.integers)} numbers are in the file, now sorting...")
            for number in self.integers:
                if number % 2 == 0:
                    self.even_integers.append(number)
                else:
                    self.odd_integers.append(number)
        elif len(self.integers) > 20:
            print(
                f"\033[91mError! \033[0m{len(self.integers)} numbers is too much! Delete some lines in numbers.txt file to continue")
        else:
            print(
                f"\033[91mError! \033[0m{len(self.integers)} numbers is too little! Add more numbers in numbers.txt file to continue")

    def odd_and_even_numbers_transformer(self):
        squared_even_integers = [self.even_integers ** 2 for number in self.integers]
        cubed_odd_integers = [self.odd_integers ** 3 for number in self.integers]
