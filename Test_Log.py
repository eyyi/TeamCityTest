__author__ = 'gabrieleyyi'

from datetime import date

import Unit_Test as un

def print_current_date():
    today = date.today()
    print "Today :\n", str(today)


def main():
    print_current_date()

def func(x):
    ##teamcity[<messageName> timestamp='timestamp' ...]
    return x + 1

def test_answer():
    assert func(3) == 4

if __name__ == '__main__':
    main()
    test_answer()

    if un.is_running_under_teamcity():
        runner = un.TeamcityTestRunner()
    else:
        runner = un.unittest.TextTestRunner()
    un.unittest.main(testRunner=runner)
