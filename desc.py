"""Descriptors and class Data"""


class Integer:
    """Desc integer"""

    def __set_name__(self, cls, name):
        self.name = name

    def __get__(self, obj, objtype):
        return obj.__dict__.get(self.name)

    def __set__(self, obj, val):
        if isinstance(val, int):
            obj.__dict__[self.name] = val
        else:
            raise ValueError("Input value is not integer")

    def __delete__(self, obj):
        del obj.__dict__[self.name]


class String:
    """Desc string"""

    def __set_name__(self, cls, name):
        self.name = name

    def __get__(self, obj, objtype):
        return obj.__dict__.get(self.name)

    def __set__(self, obj, val):
        if isinstance(val, str):
            obj.__dict__[self.name] = val
        else:
            raise ValueError("Input value is not string")

    def __delete__(self, obj):
        del obj.__dict__[self.name]


class PositiveInteger:
    """Desc positive_integer"""

    def __set_name__(self, cls, name):
        self.name = name

    def __get__(self, obj, objtype):
        return obj.__dict__.get(self.name)

    def __set__(self, obj, val):
        if isinstance(val, int):
            if val > 0:
                obj.__dict__[self.name] = val
            else:
                raise ValueError("Input value is not positive")
        else:
            raise ValueError("Input value is not integer")

    def __delete__(self, obj):
        del obj.__dict__[self.name]


class Data:
    """Class Data"""

    num = Integer()
    name = String()
    price = PositiveInteger()

    def __init__(self, num, name, price):
        self.num = num
        self.name = name
        self.price = price
