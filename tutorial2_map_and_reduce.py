from functools import reduce


def char2num(c):
    digits = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }
    return digits[c]


def str2float(s):
    t = len(s) - s.find('.') - 1
    s = s.replace('.', '')
    return reduce(lambda x, y: 10 * x + y, map(char2num, s)) / (10**t)
