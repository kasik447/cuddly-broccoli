# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.laptop = self.Laptop()
#
#     def show(self):
#         print(f'{self.name} => {self.laptop.model()}, {self.laptop.CPU()}, {self.laptop.memory()}')
#
#     class Laptop:
#         def model(self):
#             return 'HP'
#
#         def CPU(self):
#             return 'i7'
#
#         def memory(self):
#             return '16'
#
#
# s = Student('Roman')
# s.show()
# s1 = Student('Vladimir')
# s1.show()


# class Student:
#     def __init__(self, name='Roman', name1='Vladimir'):
#         self.name = name
#         self.name1 = name1
#         self.laptop = self.Laptop()
#
#     def show(self):
#         print(f'{self.name} => {self.laptop.model()}, {self.laptop.CPU()}, {self.laptop.memory()}')
#         print(f'{self.name1} => {self.laptop.model()}, {self.laptop.CPU()}, {self.laptop.memory()}')
#
#     class Laptop:
#         def model(self):
#             return 'HP'
#
#         def CPU(self):
#             return 'i7'
#
#         def memory(self):
#             return '16'
#
#
# s = Student()
# s.show()


