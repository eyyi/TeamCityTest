__author__ = 'gabrieleyyi'

from datetime import date


def print_current_date():
    today = date.today()
    print "Today :", str(today)


def main():
    print_current_date()

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4

if __name__ == '__main__':
    main()
    test_answer()
