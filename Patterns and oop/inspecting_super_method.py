""" Version 1 """
# _______________________________________________________________________________


# class Base:
#     def price(self):
#         return 10
#
#
# class Discount(Base):
#     def price(self):
#         return Base.price(self) * 0.8
#
# # The problem is that we have explicitly write the name of the ancestor 'Base'.
# # If it would be some unknown or far ancestor it will be a problem.
#
#
# a = Discount()
# print(a.price())


""" Version 2 """
# _______________________________________________________________________________


# class Base:
#     def price(self):
#         return 10
#
#
# class InterFoo(Base):
#     def price(self):
#         return Base.price(self) * 1.1
#
#
# class Discount(InterFoo):  # <--
#     def price(self):
#         return InterFoo.price(self) * 0.8  # <--
#
#
# a = Discount()
# print(a.price())


""" Version 3 """
# _______________________________________________________________________________

"""Будучи вызванным без параметров внутри какого-либо класса, super() вернет прокси-объект, методы которого будут
искаться только в классах, стоящих ранее, чем он, в порядке MRO. То есть, это будет как будто бы тот же самый
объект, но он будет игнорировать все определения из текущего класса, обращаясь только к родительским:


Calling just super() we are trying to get the object first parent class
Calling just super().price() - call the method in the first parent class as super finds the method.


Параметры super Функция может принимать 2 параметра: super([type [, object]]) Первый аргумент – это тип, 
к предкам которого мы хотим обратиться. А второй аргумент – это объект, к которому надо привязаться. Сейчас оба 
аргумента необязательные. 

Теперь Python достаточно умен, чтобы самостоятельно подставить в аргументы текущий класс и self для привязки. Но 
старая форма тоже осталась для особых случаев. Она нужна, если вы используете super() вне класса или хотите явно 
указать с какого класса хотите начать поиск методов. 

Действительно, super() может быть использована вне класса. Пример:

d = Discount()
print(super(Discount, d).price())

В этом случае объект, полученный из super(), будет вести себя как класс InterFoo (родитель Discount), хотя привязан 
он к переменной d, которая является экземпляром класса Discount. 

"""


# class Base:
#     def price(self):
#         return 10
#
#
# class InterFoo(Base):
#     def price(self):
#         return super().price() * 1.1
#
#
# class Discount(InterFoo):
#     def price(self):
#         print(f'Calling super(Discount, self).price():  '
#               f'{super(Discount, self).price()}')
#
#         print(f'Calling super(InterFoo, self).price():  '
#               f'{super(InterFoo, self).price()}')
#
#         print(f'Calling super().price():  '
#               f'{super().price()}')
#
#         print(f'Calling super():  '
#               f'{super()}')
#
#         return super().price() * 0.8

# a = Discount()
# print(a.price())


""" Version 4 """
# _______________________________________________________________________________


class A:
    def __init__(self):
        self.x = 10
#
#
# class B(A):
#     def __init__(self):
#         self.y = self.x + 5


# b = B()
# print(b.y)

# print(B().y)  # ошибка! AttributeError: 'B' object has no attribute 'x'

""" правильно:"""


class B(A):
    def __init__(self):
        super().__init__()  # <- не забудь!
        self.y = self.x + 5


print(B().y)  # 15


# Useful link:
# https://tirinox.ru/super-python/
