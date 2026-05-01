class MyLifeWriter:
    def __init__(self, file_name, text_input):
        self.file_name = file_name
        self.text_input = text_input

    def write_line(self):
        with open(self.file_name, 'a') as file:
            file.write(self.text_input + "\n")



while True:
    my_life_file = MyLifeWriter("mylife.txt", input("Enter line: "))
    my_life_file.write_line()

    user_response = input("Do you want to continue? (y/n): ")
    if user_response != "y":
        break
