from base.User import User

class Parent(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)
        self.children = []  # List of Student objects

    def add_child(self, student):
        self.children.append(student)
        print(f"{student._name} added to {self._name}'s children.")

    def view_child_progress(self, student):
        student.view_grades()
        student.view_courses()

    def track_child_attendance(self, student, course, date):
        student.record_absence(course, date)
        print(f"Attendance tracked for {student._name} in {course.name}.")

    def view_children(self):
        print(f"Children of {self._name}:")
        for child in self.children:
            print(f"- {child._name}")

