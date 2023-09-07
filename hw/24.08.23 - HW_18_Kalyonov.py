
# Homework

import os.path

# Вариант 1

dir_name = 'nested1'

objs = os.listdir(dir_name)
print(objs)
res1 = []
res2 = []

for obj in objs:
    j = os.path.join(dir_name, obj)
    if os.path.isfile(j):
        res1.append(j)
    else:
        res2.append(j)

# print(res1)
# print(res2)
print(res1 + res2)


# Вариант 2

# dir_name = 'nested1'
#
# objs = os.listdir(dir_name)
# print(objs)
# res1 = []
#
#
# for obj in objs:
#     j = os.path.join(dir_name, obj)
#     res1.append(j)
#
#
# print(sorted(res1, key=lambda s: os.path.isfile(s), reverse=True))



