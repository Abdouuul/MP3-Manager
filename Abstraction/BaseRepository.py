from abc import ABC, abstractmethod

class BaseRepository(ABC):
    def __init(self):
        self._repo : object = None
        self._connection : bool = False
        

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
