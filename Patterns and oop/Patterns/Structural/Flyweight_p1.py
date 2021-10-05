"""
The flyweight design pattern is a technique used to minimize memory usage and improve performance by introducing
data sharing between similar objects

Principal:
    A flyweight is a shared object that contains state-independent, immutable (also known as intrinsic) data. The
state-dependent, mutable (also known as extrinsic) data should not be part of flyweight because this is information
that cannot be shared, since it differs per object. If flyweight needs extrinsic data, it should be provided
explicitly by the client code.

Example:
    An example might help to clarify how the flyweight pattern can be practically used. Let's assume that we are
creating a performance-critical game, for example, a first-person shooter (FPS). In FPS games, the players (soldiers)
share some states, such as representation and behavior. In Counter-Strike, for instance, all soldiers on the same
team (counter-terrorists versus terrorists) look the same (representation). In the same game, all soldiers (on both
teams) have some common actions, such as jump, duck, and so forth (behavior). This means that we can create a
flyweight that will contain all of the common data. Of course, the soldiers also have a lot of data that is different
per soldier and will not be a part of the flyweight, such as weapons, health, location, and so on.

The Gang of Four (GoF) book lists the following requirements that need to be satisfied to effectively use the
flyweight pattern:

- The application needs to use a large number of objects.
- There are so many objects that it's too expensive to store/render them. Once the mutable state is
removed (because if it is required, it should be passed explicitly to flyweight by the client code), many groups of
distinct objects can be replaced by relatively few shared objects.
- Object identity is not important for the application. We cannot rely on object identity because object sharing causes
identity comparisons to fail (objects that appear different to the client code end up having the same identity).



The idea is that:
- we do not create new instances of a class. We just reuse some object with different parameters.

For example:
We have to use 3 figures(shape: cube, volume: 3m^3, weight: 500kg) but colours = 'white black silver'
So we create 1 instance of a cube of white colour. Use it. Change colour. Use it again.

Question: What should we do if we need that object simultaneously? Actually we can just change it quickly  
"""

from enum import Enum
import random

# First, we need an Enum parameter that describes the three different types of car that are in the car park:
CarType = Enum('CarType', 'subcompact compact suv')


class Car:
    pool = dict()  # Our cache. It is a CLASS ATTRIBUTE

    """Using the __new__() special method, which is called before __init__(), we are converting the Car class to a 
    metaclass that supports self-references. This means that cls references the Car class. When the client code 
    creates an instance of Car, they pass the type of the car as car_type. The type of the car is used to check if a 
    car of the same type has already been created. If that's the case, the previously created object is returned; 
    otherwise, the new car type is added to the pool and returned: """

    def __new__(cls, car_type):
        obj = cls.pool.get(car_type, None)
        if not obj:
            obj = object.__new__(cls)
            cls.pool[car_type] = obj
            obj.car_type = car_type
        return obj

    def render(self, color, x, y):
        Type = self.car_type
        msg = f'render a car of type {Type} and color {color} at ({x}, {y})'
        print(msg)


def main():
    # we define some variables and render a set of cars of type subcompact:
    rnd = random.Random()
    colors = 'white black silver gray red blue brown beige yellow green'.split()
    min_point, max_point = 0, 100
    car_counter = 0

    for _ in range(10):
        c1 = Car(CarType.subcompact)
        c1.render(random.choice(colors),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        car_counter += 1

    for _ in range(3):
        c2 = Car(CarType.compact)
        c2.render(random.choice(colors),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        car_counter += 1

    for _ in range(5):
        c3 = Car(CarType.suv)
        c3.render(random.choice(colors),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        car_counter += 1

    print(f'cars rendered: {car_counter}')
    print(f'cars actually created: {len(Car.pool)}')

    c4 = Car(CarType.subcompact)
    c5 = Car(CarType.subcompact)
    c6 = Car(CarType.suv)
    print(f'{id(c4)} == {id(c5)}? {id(c4) == id(c5)}')
    print(f'{id(c5)} == {id(c6)}? {id(c5) == id(c6)}')


if __name__ == '__main__':
    main()
