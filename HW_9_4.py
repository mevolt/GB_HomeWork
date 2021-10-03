class Car:
    is_police = False

    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.speed = 0


    def go(self, speed =40):
        self.speed = speed
        print(f'Car {self.name} to go, speed {self.speed}')


    def stop(self):
        self.speed = 0
        print(f'Car {self.name} is stopped')


    def turn(self, direction):
        if direction == 'left' or direction == 'right':
            print(f'Car {self.name} turns {direction}')
        else:
            print('Car turns only left or right')


    def show_speed(self):
        print(f'Car speed is {self.speed} km/h')


class TownCar(Car):

    def show_speed(self):
        if self.speed >= 61:
            print(f'Yor speed is {self.speed} km/h, you are exceeding the speed limit')
        else:
            print(f'Yor speed is {self.speed} km/h')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed >= 41:
            print(f'Your speed is {self.speed} km/h, you are exceeding the speed limit')
        else:
            print(f'Yor speed is {self.speed} km/h')


class PoliceCar(Car):
    is_police = True


auto1 = PoliceCar('white', 'Audi')
auto1.go(30)
auto2 = SportCar('Red', 'Lamborgini')
auto2.go(200)
auto2.show_speed()
auto2.turn('right')
auto3 = WorkCar('Gray', 'Geely')
auto3.go(45)
auto3.show_speed()
auto4 = TownCar('Black', 'BMW')
auto4.go(65)
auto4.show_speed()
auto4.stop()
auto4.show_speed()