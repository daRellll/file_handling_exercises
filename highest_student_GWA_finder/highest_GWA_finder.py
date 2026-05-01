class GWAAnalyzer:
    def __init__(self, file_name):
        self.file_name = file_name
        student_and_GWA_list = []

    def file_data_loader (self):
         with open(self.file_name, "r") as student_GWA_file:
              for line in student_GWA_file:
                   student_name, GWA = line.strip().split(",")
                   student_and_GWA_list.append([student_name, float(GWA)])

top_student = min(student_and_GWA_list, key=lambda x: x[1])
student_name, GWA = top_student

print(f"The top student is \033[33m{student_name}\033[0m with a GWA of \033[94m{GWA}\033[0m!")