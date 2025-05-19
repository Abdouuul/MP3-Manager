from User import User

class Account:
    def __init__(self, username, user : User):
        self._username = username
        self._user = user

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        self._username = new_username