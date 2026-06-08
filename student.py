class Student:
    def __init__(self, name, roll_no, gpa):
        self.name = name
        self.roll_no = roll_no
        self.gpa = gpa
        
    def display_report(self):
        print(f"Roll {self.roll_no}: {self.name} has a GPA of {self.gpa}")

class StudentDatabase:
    def __init__(self):
        self.all_students = [] 
        
    def add_student(self, student_object):
        self.all_students.append(student_object)
        
    def remove_student(self, roll_no):
        for s in self.all_students:
            if s.roll_no == roll_no:
                self.all_students.remove(s)
                print(f"Removed student with Roll No: {roll_no}")
                self.show_remaining_students() 
                return 
        
        
        print(f"Student with Roll No {roll_no} not found!")
        self.show_remaining_students()

   
    def show_remaining_students(self):
        if not self.all_students:
            print("The database is now empty.")
        else:
            print("Remaining students in database:")
            for student in self.all_students:
                print(f" - {student.name} (Roll: {student.role_no if hasattr(student, 'role_no') else student.roll_no})")
            print("-------------------------")


db = StudentDatabase()

s1 = Student("Ujjwal", 101, 3.8)
s2 = Student("Aayush", 102, 3.5)

db.add_student(s1)
db.add_student(s2)


db.remove_student(102)