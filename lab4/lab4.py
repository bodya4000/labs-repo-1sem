"""
модифікатори доступу: публічний і приватний


"""
class File:

    def __init__(self, id, name, description, number, string):
        self._id = id
        self._name = name
        self._description = description
        self.number = number
        self.string = string

    def __str__(self):
        return f"ID: {self._id}, Name: {self._name}, Description: {self._description}"

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def set_name(self, name):
        self._name = name

    def set_description(self, description):
        self._description = description

    def __repr__(self):
        return f"Entity(id={self._id}, name={self._name}, description={self._description})"

    def __del__(self):
        print('Destructor called')

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'description': self.description}

    def from_dict(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']


class Radiator:
    def __init__(self, power=10, color="red", producer="nokia", distance=10, number=1, string="string"):
        self.__power = power
        self.__color = color
        self.__producer = producer
        self.__distance = distance
        self.number = number
        self.string = string

    def get_power(self):
        return self.__power

    def set_power(self, power):
        self.__power = power

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_producer(self):
        return self.__producer

    def set_producer(self, producer):
        self.__producer = producer

    def get_distance(self):
        return self.__distance

    def set_distance(self, distance):
        self.__distance = distance

    def __str__(self):
        return f"radiator with power: {self.get_power()}, color: {self.get_color()}, producer: {self.get_producer()}:"

    def __del__(self):
        print('Destructor called')
