__author__ = 'gabrieleyyi'

from datetime import date


def print_current_date():
    today = date.today()
    print "Today :", str(today)


def main():
    print_current_date()


if __name__ == '__main__':
    main()
