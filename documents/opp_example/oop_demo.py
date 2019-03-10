from cat import Cat
from dog import Dog
from zoo import Zoo

if __name__ == "__main__":
    cat = Cat('Tom')
    dog = Dog('Milu')

    zoo = Zoo()
    zoo.add(cat)
    zoo.add(dog)
    zoo.show_list_animal()
    