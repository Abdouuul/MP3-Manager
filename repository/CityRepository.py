from Abstraction.BaseRepository import BaseRepository as br
from Model.City import City
class CityRepository(br):

    @staticmethod
    def get_by_id(id):
        try:
            user = CityRepository.session.query(City).get(id)
            return user
        except:
            print('City not found, or database not connected')

    @staticmethod
    def get_all():
        try:
            cities = CityRepository.session.query(City).all()
            return cities
        except:
          print('An exception occurred when getting all cities')

    def add(city):
        try:
          CityRepository.session.add(city)
          CityRepository.session.commit()
          print('User added successfully')
        except:
          print('An exception occurred when adding new city')

    def update(city):
        try:
            CityRepository.session.update(city)
            CityRepository.session.commit()
        except:
            print('An exception occurred when updating city')

    def delete():
        try:
            CityRepository.session.delete()
            CityRepository.session.commit()
            print('City deleted successfully')
        except:
            print('An exception occurred when deleting city')