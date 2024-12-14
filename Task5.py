class Tomato:

    # Стадии дозривання помидора
    states = {0: 'nothing', 1: 'flower', 2: 'green_tomato', 3: 'red_tomato'}

    def __init__(self, index):
        self.__index = index
        self._state = 0

    # Перехид до наступнои стадии дозривання 
    def grow(self):
        self.__change_state()

    # Перевирка, чи дозвир томат
    def is_ripe(self):
        if self._state == 3:
            return True
        return False
    
    # Захищени методи

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Tomato {self.__index} is {Tomato.states[self._state]}')
        
class TomatoBush:

    # Створюемо список об'эктив класу Tomato
    def __init__(self, num):
        self.tommatoes = [Tomato(index) for index in range(0, num)]

    # Перекладаэмо вси томати зи списку на наступний етап дозривання
    def grow_all(self):
        for tomato in self.tommatoes:
            tomato.grow()

    # Перевиряемо, чи вси помидори дозрили
    def all_are_ripe(self):
        return all([Tomato.is_ripe() for tomato in self.tommatoes])
    
    # Збираэмо врожай
    def givr_away_all(self):
        self.tommatoes = []

class Gardener:

    # Видыэмо содивнику рослину для догляду
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    # Доглядаэмо рослину
    def work(self):
        print('Gardener is working...')
        self._plant.grow_all()
        print('Gardener finished')

    # Збираэмо врожай
    def harvest(self):
        print('Garden is harvesting...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Harvesting is finished')
        else:
            print('Too early! Your plant is green and not ripe.')

    #Статичний метод
    # Виводить довидку з садивництва
    @staticmethod
    def knowledge_base():
        print('''Harvest time for tomatoes should ideally occur
when the fruit is a mature green and
then allowed to ripen off the vine.
This prevents splitting or bruising
and allows for a measure of control over the ripening process.''')

# Тести
if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Emilio', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()