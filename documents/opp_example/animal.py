class Animal(object):
    __name = None

    def __init__(self, name):
        self.__name = name

    def say_hello(self):
        raise NotImplementedError()

    def get_name(self):
        return self.__name
