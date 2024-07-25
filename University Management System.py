class University:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def get_departments(self):
        return self.departments

class Department:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.professors = []

    def add_course(self, course):
        self.courses.append(course)

    def add_professor(self, professor):
        self.professors.append(professor)

    def get_courses(self):
        return self.courses

    def get_professors(self):
        return self.professors

class Course:
    def __init__(self, code, name, credits):
        self.code = code
        self.name = name
        self.credits = credits
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)

    def get_students(self):
        return self.students

class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Student(Person):
    def __init__(self, name, id, year):
        super().__init__(name, id)
        self.year = year
        self.courses = []

    def enroll_in_course(self, course):
        self.courses.append(course)
        course.enroll_student(self)

    def get_courses(self):
        return self.courses

class Professor(Person):
    def __init__(self, name, id, title):
        super().__init__(name, id)
        self.title = title
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)

    def get_courses(self):
        return self.courses

#  instances of these classes

# Create a university
university = University("Virtual University")

# Create departments
cs_department = Department("Computer Science")
math_department = Department("Mathematics")

# Add departments to the university
university.add_department(cs_department)
university.add_department(math_department)

# Create courses
c01 = Course("C-01", "Introduction to Computer Science", 3)
ma01 = Course("M-01", "Calculus I", 4)

# Add courses to departments
cs_department.add_course(c01)
math_department.add_course(ma01)

# Create professors
prof_Khan = Professor("Dr. Khan", "P-01", "Professor")
prof_Rehman = Professor("Dr. Rehman", "P-02", "Associate Professor")

# Assign courses to professors
prof_Khan.assign_course(c01)
prof_Rehman.assign_course(ma01)

# Add professors to departments
cs_department.add_professor(prof_Khan)
math_department.add_professor(prof_Rehman)

# Create students
student_Humza = Student("Humza", "S-01", "Sophomore")
student_Faisal = Student("Faisal", "S-02", "Freshman")

# Enroll students in courses
student_Humza.enroll_in_course(c01)
student_Faisal.enroll_in_course(ma01)

# Retrieve and print information
print(f"University: {university.name}")
for dept in university.get_departments():
    print("")
    print(f"Department: {dept.name}")
    print("\nCourses:")
    for course in dept.get_courses():
        print(f"  {course.code}: {course.name}")
        print("  Enrolled students:")
        for student in course.get_students():
            print(f"    {student.name} ({student.id})")
    print("")
    print("Professors:")
    for prof in dept.get_professors():
        print(f"  {prof.name} ({prof.id}): {prof.title}")
