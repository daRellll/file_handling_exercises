class MyLifeWriter:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_line(self, text):
        with open(self.file_name, 'a') as file:
            text = input("Enter line: ")
            file.write(text + "\n")

my_life_file = MyLifeWriter("my_life.txt")

while True:
    my_life_file.write_line()

    user_response = input("Do you want to continue? (y/n): ")