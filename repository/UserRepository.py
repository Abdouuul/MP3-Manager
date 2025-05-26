from Abstraction.BaseRepository import BaseRepository as br
from Model.User import User
from extensions import db

class UserRepository(br):

    def get_by_id(id):
        try:
            user = UserRepository.session_manager.query(User).get(id)
            return user
        except:
            print('User not found, or database not connected')

    
    def get_all():
        try:
            users = User.query.all()
            return users
        except Exception as e:
          print('An exception occurred when getting all users :',e)

    def add(self, user):
        try:
          self.session_manager.add(user)
          self.session_manager.commit()
          print('User added successfully')
        except:
          print('An exception occurred when adding new user')

    def update(self, user):
        try:
            self.session_manager.update(user)
            self.session_manager.commit()
        except:
            print('An exception occurred when updating user')

    def delete(self, user):
        try:
            self.session_manager.delete(user)
            self.session_manager.commit()
            print('User deleted successfully')
        except:
            print('An exception occurred when deleting user')