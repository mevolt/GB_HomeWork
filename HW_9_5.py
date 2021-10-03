class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Start drawing')


class Pen(Stationery):

    def draw(self):
        print(f'{self.title} draw blue line')


class Pencil(Stationery):

    def draw(self):
        print(f'{self.title} draw gray line')


class Handle(Stationery):

    def draw(self):
        print(f'{self.title} draw black line')


object1 = Pen('Pen')
object1.draw()
object2 = Pencil('Pencil')
object2.draw()
object3 = Handle('Handle')
object3.draw()