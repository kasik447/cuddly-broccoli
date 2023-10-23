class Square:
    def __init__(self, a):
        self.a = a

    def get_perimetr(self):
        return 4 * self.a


if __name__ == '__main__':
    print('*' * 20)
    s1 = Square(10)
    print(s1.get_perimetr())
    print('*' * 20)
