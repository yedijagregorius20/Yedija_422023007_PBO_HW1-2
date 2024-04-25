from base.User import User

class Operator(User):
    def __init__(self, user_id, name, email, password, operator_id):
        super().__init__(user_id, name, email, password)
        self.operator_id = operator_id

    def provide_technical_support(self):
        # Logic for providing technical support
        print("Technical support provided.")

    def maintain_system(self):
        # Logic for system maintenance
        print("System maintenance performed.")

