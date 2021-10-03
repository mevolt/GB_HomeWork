class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        print(f"Worker: {self.name} {self.surname}")

    def get_position(self):
        print(f'Position: {self.position}')

    def total_income(self):
        print(f'Income: {sum(self._income.values())}')


worker = Position('Pavel', 'Malanchew', 'TestEngineer', 120000, 100000)
worker.get_full_name()
worker.get_position()
worker.total_income()