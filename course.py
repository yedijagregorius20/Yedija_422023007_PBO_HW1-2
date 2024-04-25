class Course:
    def __init__(self, course_id, name, description):
        self.course_id = course_id
        self.name = name
        self.description = description
        self.students_enrolled = []  # List of Student objects
        self.course_materials = []

    def add_student(self, student):
        self.students_enrolled.append(student)
        print(f"{student._name} added to {self.name}.")

    def remove_student(self, student):
        self.students_enrolled.remove(student)
        print(f"{student._name} removed from {self.name}.")

    def update_course_material(self, course_material):
        self.course_materials.append(course_material)
        print("Course material updated.")

    def view_students_enrolled(self):
        print(f"Students enrolled in {self.name}:")
        for student in self.students_enrolled:
            print(f"- {student._name}")

    def remove_student_by_id(self, student_id):
        for student in self.students_enrolled:
            if student._user_id == student_id:
                self.students_enrolled.remove(student)
                print(f"{student._name} removed from {self.name}.")
                return
        print("Student not found in the course.")

