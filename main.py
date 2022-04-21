"""Module for Metaclass CustomMeta"""


class CustomMeta(type):
    """Metaclass CustomMeta"""
    def __new__(cls, name, bases, classdict):
        attr = []
        for key in classdict:
            if not key[:2] == key[-2:] == "__":
                attr.append(key)

        for key in attr:
            classdict["custom_" + key] = classdict[key]
            del classdict[key]

        return super().__new__(cls, name, bases, classdict)

    def change_name_attr(cls, attr, val):
        """Change attr on custom_..."""
        if not attr[:2] == attr[-2:] == "__":
            cls.__dict__["custom_" + attr] = val

    def __prepare__(cls, *args):
        return {'__setattr__': CustomMeta.change_name_attr}


class CustomClass(metaclass=CustomMeta):
    """Class Customclass"""
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        """line func"""
        return 100

    def __str__(self):
        return "Custom_by_metaclass"
