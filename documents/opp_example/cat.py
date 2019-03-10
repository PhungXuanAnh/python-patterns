from animal import Animal


class Cat(Animal):

    def __init__(self, name):
        super(Cat, self).__init__(name)

    def say_hello(self):
        print('Hi, I am {}'.format(self.get_name()))

