"""
The proxy design pattern gets its name from the proxy (also known as surrogate) object used to perform an
important action before accessing the actual object.

In Proxy class we have to provide interface similar to the real object class but can also extend it or make some
pre-requirements available.

Use cases:
- We can make cache of some queries from DB and check it, so save time on queries. ORM systems
- We can log some input or output of real object but to make it clear and pretty.
- Prevent access for unauthorized users. Like we have some object that influence OS so we don't want everybody to have
access to it. We make some validation before permitting the access.

Pros:
- can control service actions and objects and client will not notice this

Cons:
- longer time response

Very similar:
- Proxy
- Decorator
- Adapter
- Facade ?
"""
from abc import ABC, abstractmethod


class Subject(ABC):
    """
        Define the common interface for RealSubject and Proxy so that a
        Proxy can be used anywhere a RealSubject is expected.
    """
    @abstractmethod
    def request(self) -> None:
        pass


class RealSubject(Subject):
    """
       Define the real object that the proxy represents.
    """
    def request(self) -> None:
        print("RealSubject: Handling request")


class Proxy(Subject):
    """
        Maintain a reference that lets the proxy access the real subject.
        Provide an interface identical to Subject's.
    """
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print('Proxy: Checking access prior to firing the real request')
        return True

    def log_access(self) -> None:
        print('Proxy: Logging the time of request')


def client_code(subject: Subject) -> None:
    subject.request()


if __name__ == '__main__':
    real_Subject = RealSubject()
    print("Client: Executing the same client code with a proxy")
    proxy = Proxy(real_Subject)
    client_code(proxy)
