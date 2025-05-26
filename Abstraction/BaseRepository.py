from abc import ABC, abstractmethod
from extensions import db

class BaseRepository(ABC):
    session_manager = db.session        


    @abstractmethod
    def get_by_id():
        pass

    @abstractmethod    
    def get_all():
        pass

    @abstractmethod
    def add():
        pass

    @abstractmethod
    def update():
        pass

    @abstractmethod
    def delete():
        pass
