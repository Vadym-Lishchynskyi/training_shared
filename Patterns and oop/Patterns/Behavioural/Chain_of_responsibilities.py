"""
Chain of Responsibility
Can be of two types:
- pass all mediators(посредник) to the end
- quite as soon as object find the proper mediator(посредник)

Idea: When developing an application, most of the time we know which method should satisfy a particular request in
advance. However, this is not always the case. For example, think of any broadcast computer network, such as the
original Ethernet implementation.

World example:
- in hospital you go to every doctor one by one as soon as treat your problem
- you ask support in bank our IT firm or whatever.

Usage:
- when we want to give a chance to multiple objects to satisfy a single request
- when we don't know in advance which object (from a chain of objects) should process a specific request.
- когда программа должна обрабатывать разнообразные запросы несколькими способами, но зарание неизвестно
какие конкретно запросы будут приходить и какаие обработчики для них понадобяться.
- когда важно что-бы оброботчики включались одиин за другим в строгом порядке.

Pros:
- уменьшает зависимость между клиентом и оброботчиком
- реализует принцып единственной обязаности (ответственности)
- реализует принцып открытости/закрытости

Note that the client code only knows about the first processing element, instead of having references to all of them,
and each processing element only knows about its immediate next neighbor (called the successor)

"""
from abc import ABC, abstractmethod
from typing import Optional, Any


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler):
        self._next_handler = handler

        # Возврат оброботчика отсюда позволяет связать оброботчики простом способом, вот так:
        # monkey.set_next(squirrel)>set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)


class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == 'Banana':
            return f'Monkey:I will eat the {request}'
        else:
            # print(f'Super: {super().handle(request)}')
            return super().handle(request)


class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == 'Nut':
            return f'Squirrel:I will eat the {request}'
        else:
            return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == 'Meat':
            return f'Dog:I will eat the {request}'
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    for food in ['Nut', 'Banana', 'Meat', 'Cup of coffee']:
        print(f'Client who wants a {food}')
        result = handler.handle(food)
        if result:
            print(f'{result}', end='')
        else:
            print(f'{food} was left untouched.', end='')


monkey = MonkeyHandler()
squirrel = SquirrelHandler()
dog = DogHandler()

monkey.set_next(squirrel).set_next(dog)

print("Chain: Monkey -> Squirrel -> Dog")
client_code(monkey)
print('\n')

print('SubChain: Squirrel -> Dog')
client_code(squirrel)
