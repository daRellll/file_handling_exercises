class OddAndEvenNumbersSorterAndTransformer:
    def __init__(self, integers_file):
        self.integers_file = integers_file
        self.integers = []
        self.odd_integers = []
        self.even_integers = []
        self.squared_even_integers = []
        self.cubed_odd_integers = []

    def integers_file_data_loader(self):
        with open(self.integers_file) as integers_file:
            for line in integers_file:
                self.integers.append(int(line.strip()))

    def odd_and_even_integers_sorter(self):
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

    def odd_and_even_integers_transformer(self):
        for number in self.odd_integers:
            cubed_integer = number ** 3
            self.even_integers.append(cubed_integer)

        for number in self.even_integers:
            squared_integer = number ** 2
            self.even_integers.append(squared_integer)

    def odd_integers_file_data_encoder(self):
        with open("triple.txt", "w") as odd_integers_file:
            for number in self.cubed_odd_integers:
                odd_integers_file.write(f"{number}\n")

    def even_integers_file_data_encoder(self):
        with open("double.txt", "w") as even_integers_file:
            for number in self.squared_even_integers:
                even_integers_file.write(f"{number}\n")

integers_transformer = OddAndEvenNumbersSorterAndTransformer("integers_file.txt")
integers_transformer.integers_file_data_loader()
integers_transformer.odd_and_even_integers_sorter()
integers_transformer.odd_and_even_integers_transformer()
integers_transformer.odd_integers_file_data_encoder()
integers_transformer.even_integers_file_data_encoder()