from werkzeug.security import generate_password_hash, check_password_hash

class User:

    def __init__(self,id,name,surname,username,password):
        self.id = id
        self.name = name
        self.surname = surname
        self.username = username
        self.password = password
