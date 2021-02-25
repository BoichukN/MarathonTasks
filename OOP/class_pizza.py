# Create a Pizza class with the attributes order_number and ingredients (which is given as a list).
# Only the ingredients will be given as input.
# You should also make it so that its possible to choose a ready made pizza flavour
# rather than typing out the ingredients manually! As well as creating this Pizza class,
# hard-code the following pizza flavours.

class Pizza:
    counter = 0

    def __init__(self, ingredients=list):
        self.ingredients = ingredients
        Pizza.counter += 1
        self.order_number = Pizza.counter

    @staticmethod
    def hawaiian():
        return Pizza(['ham', 'pineapple'])

    @staticmethod
    def meat_festival():
        return Pizza(['beef', 'meatball', 'bacon'])

    @staticmethod
    def garden_feast():
        return Pizza(['spinach', 'olives', 'mushroom'])
