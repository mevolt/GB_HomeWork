class Road:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def mass(self, weight=25, thickness=5):
        return(f'Asphalt mass: {self.__width * self.__length * weight * thickness}')


road = Road(300, 200)
print(road.mass())


