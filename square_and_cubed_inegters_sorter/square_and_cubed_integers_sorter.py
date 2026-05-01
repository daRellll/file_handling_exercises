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

    