from abc import ABC, abstractmethod
from copyreg import constructor


# Creators
class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def print_holiday_msg(self, name):
        product = self.factory_method(name)
        msg = product.create_msg()
        print(msg)


class ChristmasCreator(Creator):

    def factory_method(self, name):
        return ChristmasMsg(name)


class HalloweenCreator(Creator):

    def factory_method(self, name):
        return HalloweenMsg(name)


# Products
class HolidayMsg(ABC):

    @abstractmethod
    def create_msg(self):
        pass


class ChristmasMsg(HolidayMsg):

    def __init__(self, name):
        self.name = name

    def create_msg(self):
        return f"Merry Christmas, {self.name}!"


class HalloweenMsg(HolidayMsg):

    def __init__(self, name):
        self.name = name

    def create_msg(self):
        return f"Trick or treat, {self.name}!"


def client_code(creator, name):
    creator().print_holiday_msg(name)
