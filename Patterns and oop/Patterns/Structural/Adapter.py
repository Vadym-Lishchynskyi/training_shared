"""
Adapter + Zope

The adapter pattern is a structural design pattern that helps us make two incompatible interfaces compatible.

If we have an old component and we want to use it in a new system, or a new component that we want to use in an old
system, the two can rarely communicate without requiring any code changes. But, changing the code is not always
possible, either because we don't have access to it, or because it is impractical. In such cases, we can write an
extra layer that makes all the required modifications for enabling the communication between the two interfaces. This
layer is called an adapter.


Zope ....


"""


class Club:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'the club {self.name}'

    def organize_event(self):
        return 'hires an artist to perform for the people'


"""The client code, using these classes, only knows how to call the organize_performance() method (on the Club 
class); it has no idea about play() or dance() (on the respective classes from the external library). But Musician 
has method play() to start performance. Dancer has method dance()  to start performance. 

How can we make the code work without changing the Musician and Dancer classes?


"""


class Musician:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'the musician {self.name}'

    def play(self):
        return 'plays music'


class Dancer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'the dancer {self.name}'

    def dance(self):
        return 'does a dance performance'


"""
Adapters to the rescue! We create a generic Adapter class that allows us to adapt a 
number of objects with different interfaces, into one unified interface. 


The obj argument of the __init__() method is the object that we want to adapt, and 
adapted_methods is a dictionary containing key/value pairs matching the method the 
client calls and the method that should be called.
"""


class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


def main():
    objects = [Club('Jazz Cafe'), Musician(
        'Roy Ayers'), Dancer('Shane Sparks')]

    for obj in objects:
        if hasattr(obj, 'play') or hasattr(obj, 'dance'):
            if hasattr(obj, 'play'):
                adapted_methods = dict(organize_event=obj.play)
            elif hasattr(obj, 'dance'):
                adapted_methods = dict(organize_event=obj.dance)

            # referencing the adapted object here
            obj = Adapter(obj, adapted_methods)

        print(f'{obj} {obj.organize_event()}')


if __name__ == '__main__':
    main()
