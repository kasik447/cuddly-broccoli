# Множественное наследование

# class Creature:
#
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + ' is sleeping')
#
#
# class Pet(Creature):
#     def __init__(self, age):
#         self.age = age
#         print('Инициализатор класса Pet')
#
#     def play(self):
#         print(self.name + ' is playing')
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + ' is barking')
#
#
# dog = Dog('Buddy')
# dog.bark()
# # dog.play()
# # dog.sleep()


class A:
    def __init__(self):
        print('Инициализатор класса А')

class B(A):
    def __init__(self):
        print('Инициализатор класса B')

class C(A):
    def __init__(self):
        print('Инициализатор класса C')

class D(B, C):
    def __init__(self):
        print('Инициализатор класса D')


d = D()
print(D.mro())
print(D.__mro__)


