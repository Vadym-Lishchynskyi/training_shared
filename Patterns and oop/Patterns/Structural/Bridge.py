"""

Using the bridge pattern is a good idea when you want to share an implementation among multiple objects. Basically,
instead of implementing several specialized classes, defining all that is required within each class, you can define
the following special components:

- An abstraction that applies to all the classes
- A separate interface for the different objects involved
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Implementation(ABC):
    """
    This class like a TV. It obligates all instances of a TV to implement the interface. They must have
    operation_implementation method.
    """
    @abstractmethod
    def operation_implementation(self) -> str:
        pass


class ConcreteImplementationA(Implementation):
    """ Concrete TV 1 which you can turn with any пульт..."""
    def operation_implementation(self) -> str:
        return 'Here is the result of the platform A'


class ConcreteImplementationB(Implementation):
    """ Concrete TV 2 which you can turn with any пульт..."""
    def operation_implementation(self) -> str:
        return 'Here is the result of the platform B'


class Abstraction:
    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f'Abstraction: Base operation with:'
                f'{self.implementation.operation_implementation()}')


class ExtendedAbstraction(Abstraction):
    def operation(self) -> str:
        return (f'ExtendedAbstraction: Extended operation with:'
                f'{self.implementation.operation_implementation()}')


def client_code(abstraction: Abstraction) -> None:
    print(abstraction.operation(), end='')


implementation = ConcreteImplementationA()
abstraction = Abstraction(implementation)
client_code(abstraction)

print()

implementation = ConcreteImplementationB()
abstraction = Abstraction(implementation)
client_code(abstraction)
