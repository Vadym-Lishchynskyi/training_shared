"""

!!!!! Can be ANTI-PATTERN !!!!!

Problems it solve:
- guaranties that there is only one instance of a class (that is where the name came from)
- provides global point(scope)
- control over global variables

World examples:
Only one phone station in the town. SO to call your friend you need to work only through this one unique station.
Or kind of government that can be only unique in your particular country.

Programming example:
DB connection - it can be only one and should be available from a global scope everywhere.

Problems:
We can't test it properly as we have only One object so - only one state of that object. So on wee have to create
mocks and play around with testing.

We can also make it with:
- decorators
- some how with 'constructor' check what is constructor!
"""


class SingletonMeta(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwargs)
            cls._instance[cls] = instance
        return cls._instance[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass


s1 = Singleton()    # after such syntax 'Singleton()' method __call__() arose
s2 = Singleton()

if id(s1) == id(s2):
    print("Singleton works - both variables contains the same instances")
else:
    print("Singleton failed, variables contains different instances")

