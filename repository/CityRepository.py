from Abstraction.BaseRepository import BaseRepository as br
from Model.City import City
class CityRepository(br):

    def get_by_id(self, id):
        try:
            user = self.session_manager.query(City).get(id)
            return user
        except:
            print('City not found, or database not connected')

    def get_all(self):
        try:
            cities = self.session_manager.query(City).all()
            return cities
        except Exception as e:
          print('An exception occurred when getting all cities : ', e)

    def add(self, city):
        try:
          self.session_manager.add(city)
          self.session_manager.session.commit()
          print('User added successfully')
        except:
          print('An exception occurred when adding new city')

    def update(self, city):
        try:
            self.session_manager.update(city)
            self.session_manager.commit()
        except:
            print('An exception occurred when updating city')

    def delete(self):
        try:
            self.session_manager.delete()
            self.session_manager.commit()
            print('City deleted successfully')
        except:
            print('An exception occurred when deleting city')