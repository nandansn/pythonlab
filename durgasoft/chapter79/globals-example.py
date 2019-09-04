from abc import *

class DB(ABC):
    @abstractmethod
    def connect(self):
        pass


class Oracle(DB):
    def connect(self):
        print('oracle db connection')


class MySQL(DB):
    def connect(self):
        print('mysql db connection')


dbName = input('Enter DB Name:')
className = globals()[dbName]

print(type(className))

x=className()
x.connect()