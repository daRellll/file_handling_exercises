student_and_GWA_list = []

with open("student_GWA_list.txt", "r") as student_GWA_file:
     for line in student_GWA_file:
          student_name, GWA = line.strip().split(",")
          student_and_GWA_list.append([student_name, float(GWA)])

top_student = min(student_and_GWA_list, key=lambda x: x[1])
student_name, GWA = top_student

print(f"The top student is {student_name} with a GWA of {GWA}!")