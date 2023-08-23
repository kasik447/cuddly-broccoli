# Home_work


# def outer(a, b, c):
#
#     def inner(x, y):
#         return x * y
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))


# s = 0
#
#
# def outer(a, b, c):
#
#     def inner(x, y):
#         return x * y
#     global s
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))


# def outer(a, b, c):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s = 2 * ((a * b) + (a * c) + (b * c))
#
#     inner()
#     return s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))
