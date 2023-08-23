s = 'I am learning Python. hello, WORLD'
print(s)
a = s.find('h')
b = s.rfind('h')
c = s[a:b]
reversed_c = c[::-1]
# print(reversed_c)
s = s[:s.find('h') + 1] + reversed_c + s[s.rfind('h') + 1:]
print()
print(s)


