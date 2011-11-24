# stolen by dorkitude from StackOverflow:
# http://stackoverflow.com/questions/5189699/how-can-i-make-a-class-property-in-python


class ClassPropertyError(Exception):
    pass




class ClassPropertyDescriptor(object):

    def __init__(self, fget, fset=None):
        self.fget = fget
        self.fset = fset

    def __get__(self, obj, klass=None):
        if klass is None:
            klass = type(obj)
        return self.fget.__get__(obj, klass)()


def classproperty(func):
    if not isinstance(func, (classmethod, staticmethod)):
        func = classmethod(func)

    return ClassPropertyDescriptor(func)
