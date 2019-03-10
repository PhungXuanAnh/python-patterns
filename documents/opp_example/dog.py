from animal import Animal


class Dog(Animal):

    def __init__(self, name):
        super(Dog, self).__init__(name)

    def say_hello(self):
        print('Hello, My name is {}'.format(self.get_name()))