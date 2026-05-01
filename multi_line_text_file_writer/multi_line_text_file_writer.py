class MyLifeWriter:
    def __init__(self, file_name):
        self.file_name = file_name

    def user_write(self, text):
        with open(self.file_name, 'a') as file:
            text = input("Enter line: ")
            