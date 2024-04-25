class Attendance:
    def __init__(self, student_id, course_id, date):
        self.student_id = student_id
        self.course_id = course_id
        self.date = date

    def record_absence(self):
        print(f"Absence recorded on {self.date}.")

