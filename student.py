from base.User import User
from attendance import Attendance

class Student(User):
    def __init__(self, user_id, name, email, password, enrollment_id):
        super().__init__(user_id, name, email, password)
        self.enrollment_id = enrollment_id
        self.courses = []  # List of Course objects
        self.grades = []   # List of Grade objects
        self.absences = []  # List of Attendance objects

    def enroll_in_course(self, course):
        self.courses.append(course)
        course.add_student(self)
        print(f"{self._name} enrolled in {course.name}.")

    def view_grades(self):
        for grade in self.grades:
            print(f"Course: {grade.course_id}, Grade: {grade.letter_grade}")

    def view_courses(self):
        for course in self.courses:
            print(f"Enrolled in: {course.name}")

    def record_absence(self, course, date):
        attendance = Attendance(self._user_id, course.course_id, date)
        attendance.record_absence()
        self.absences.append(attendance)
        print(f"Absence recorded for {self._name} in {course.name}.")

