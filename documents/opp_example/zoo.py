class Zoo(object):

    __animals = []

    def add(self, animal):
        self.__animals.append(animal)

    def remove(self, animal):
        self.__animals.remove(animal)

    def show_list_animal(self):
        for animal in self.__animals:
            animal.say_hello()