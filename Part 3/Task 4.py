# В первой строке дано три числа, соответствующие некоторой дате - год, месяц и день.
# Во второй строке дано одно число - число дней. Вычислите и выведите год, месяц и день даты, которая наступит,
# когда с момента исходной даты пройдет указанное число дней.
# Вводятся список целых чисел. Затем на отдельной строке одно целое число.
import sys
import datetime


def date1():
    call = (tuple(map(int, line.split())) for line in sys.stdin)
    year, month, day = next(call)

    return datetime.datetime(year, month, day)

date2 = date1()
days2add = datetime.timedelta(int(input()))
newdate = date2 + days2add
print(newdate.year, newdate.month, newdate.day)
