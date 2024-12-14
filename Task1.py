class Soda:
    """Вода"""

    def __init__(self, ingredient):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def show_my_drink(self):
        if self.ingredient:
            print(f'Газована вода та {self.ingredient}')
        else:
            print('Звичайна газована вода')