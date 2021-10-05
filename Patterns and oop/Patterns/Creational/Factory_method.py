from abc import ABC, abstractmethod

"""
!!!Usage
Just imagine:
You are a wealthy owner of a logistic company that transfer some goods by cars to different parts of the world
(Nova Poshta owner) 

You were doing your business good enough and decided to expand and add ships to your system so you can transfer goods
to different continents by ships. There are two solutions:
    - you can add lots of 'if' statements and it would work fine until you wouldn't want to add planes for example. In
        this case it will be necessary to do all the work again and again
    - you can use 'Factory_method' pattern so, you will write once more complex code but everything needed to add new
        way of transporting is to create another 'Creator' class (which you steel would need for new type of shipping) 
        and add necessary implementations of same method 'move' or whatever else you need.   
        
Key1: The pattern will work only if methods factory_method() and product.operation() are implied. But all that are done 
within abstract methods so idea would remind you.

Key2: Using such patterns we are not linked to the type of the objects or classes we create - methods like interface.


Usage:
1) When we don't know types linking of objects we gonna create and work with beforehand.
2) When we want to give users or further developers - the ability to expand code of your framework or library.

Pros:
1) Reduce class(that has to be creates) from linking it to some particular type.
    All communication with the product classes is actually made via the interface provided by abstract methods.
2) Detach code (where create the product) to one place, to make the code easier to support.
3) Give the ability to extend code easily.
4) Establish Open/close principle (one of SOLID principles) 
5) Other components like ConcreteCreator1 and ConcreteProduct1 will be untouched and whatever you do with other 
    components have no influence on this one.
"""


# Factory method
class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        # Call fabric method to get product-object (object of a product)
        product = self.factory_method()

        # Actually work with this product
        result = f"Creator: The some creator's code has just worked with {product.operation()}"

        return result


class Product(ABC):
    @abstractmethod
    def operation(self):
        pass


# That is actually our plane, car, ship or whatever we would like to be created to transit our goods
class ConcreteCreator1(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):

    def factory_method(self) -> Product:
        return ConcreteProduct2()


# That is actually our plane, car, ship or whatever we would like to be created to transit our goods
class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


def client_code(creator: Creator) -> None:

    print(f"Client: I'm not aware of the creator's class, but it still works"
          '\n'
          f"{creator.some_operation()}", end="")


print("App: Launched with the ConcreteCreator1")
client_code(ConcreteCreator1())
print('\n')

print("App: Launched with the ConcreteCreator2")
client_code(ConcreteCreator2())
