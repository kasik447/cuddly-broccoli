
import json
from random import choice


def gen_person():
    main_key = ''
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'e']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(main_key) != 12:
        main_key += choice(nums)
    # print(main_key)

    while len(name) != 7:
        name += choice(letters)
    # print(name)

    while len(tel) != 10:
        tel += choice(nums)
    # print(tel)

    person = {
        'name': name,
        'tel': tel
    }

    key_person = {
        main_key: person
    }
    return key_person


def write_json(person_dict):
    try:
        data = json.load(open('persons_hw.json'))
    except FileNotFoundError:
        data = {}

    data.update(person_dict)
    with open('persons_hw.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person())
