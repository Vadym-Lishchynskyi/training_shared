"""
Factory + Flyweight

"""

import json
from typing import Dict


class Flyweight:
    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: str) -> None:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f'Flyweight: Displays shared state ({s}) and unique ({u}) state.', end='')


class FlyweightFactory:
    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: Dict) -> None:
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: Dict) -> str:
        return '_'.join(sorted(state))

    def get_flyweight(self, shared_state: Dict) -> Flyweight:
        key = self.get_key(shared_state)

        if not self._flyweights.get(key):
            print("FlyweightFactory: Can't find a flyweight, creating a new one.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: Reusing existing flyweight")

        return self._flyweights[key]

    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f'FlyweightFactory: I have {count} flyweights')
        print("\n".join(map(str, self._flyweights.keys())), end='')


def add_car_to_police_database(
        factory: FlyweightFactory,
        plates: str,
        owner: str,
        brand: str,
        model: str,
        color: str) -> None:
    flyweight = factory.get_flyweight([brand, model, color])

    # Клиентский код либо сохраняет, либо вычисляет внешнее состояние и передает его методам легковеса.
    flyweight.operation([plates, owner])


if __name__ == '__main__':
    """
    Клиентский код обычно создает кучу предварительно заполненых легковесов на этапе инициализации прилодения.
    """

    factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mersedes Benz", "C300", "black"],
        ["Mersedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
    ])

    factory.list_flyweights()

    add_car_to_police_database(factory, "CLR234IR", "James Doe", "BMW", "M5", "red")
    add_car_to_police_database(factory, "CLR234IR", "James Doe", "BMW", "X1", "blue")

    print()

    factory.list_flyweights()