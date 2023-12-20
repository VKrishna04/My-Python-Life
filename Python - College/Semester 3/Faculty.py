# Write a program that uses a class attribute to define some default titles for faculty in a college. Display the name along with title and department of the college
class Faculty:
    def __init__(self, name, department, title="Dr."):
        self.name = title + name
        self.department = department

    def display(self):
        print("Name: ", self.name)
        print("Department: ", self.department)


name = input("Enter name: ")
department = input("Enter department: ")
f1 = Faculty(name, department)
f1.display()
