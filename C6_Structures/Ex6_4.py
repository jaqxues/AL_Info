a = int(input("Enter year: "))
d = int(input("Enter day of year: "))
m = 0


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


days_in_months = [31, 29 if is_leap_year(a) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while d > days_in_months[m]:
    d -= days_in_months[m]
    m += 1

print(a, m, d)
