from base.User import User
from student import Student
from professor import Professor
from operatorr import Operator
from parent import Parent

class Admin(User):
    def create_user_account(self, user_type, *args):
        # Polymorphism
        if user_type == "student":
            return Student(*args)
        elif user_type == "professor":
            return Professor(*args)
        elif user_type == "operator":
            return Operator(*args)
        elif user_type == "parent":
            return Parent(*args)
        else:
            return None

