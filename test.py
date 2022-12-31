from itertools import zip_longest


def make_dict(fieldnames, values):
    return dict(zip_longest(fieldnames, values, fillvalue=None))


sentence = "I want to be a Python developer"
print(sentence[5])

sentence.split()
try:
    print(sentence[7])
except IndexError:
    print('Ошибка индексирования')


def tuples_list(a, b):
    while len(a) != len(b):
        if len(a) < len(b):
            a.append('N/A')
        elif len(a) > len(b):
            b.append('N/A')
    return [tuple(a), tuple(b)]


file = open('filename.txt')
for word in file:
    count = 0
    if word == 'червяк':
        count += 1