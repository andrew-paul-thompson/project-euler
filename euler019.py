month_days = {0: 31, 1: 28, 2: 31, 3: 30, 4: 31, 5: 30, 6: 31, 7: 31, 8: 30, 9: 31, 10: 30, 11: 31}
days_in_a_week = 7
months_in_a_year = 12


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def get_month_days(month, year):
    days = month_days[month]
    if is_leap_year(year) and month == 1:
        days += 1
    return days


current_year = 1900
current_month = 0
current_day = 0
current_weekday = 1
sundays_on_first_of_month = 0
while current_year < 1901:
    current_day = (current_day + 1) % get_month_days(current_month, current_year)
    current_weekday = (current_weekday + 1) % days_in_a_week
    current_month = (current_month + 1) % months_in_a_year if current_day == 0 else current_month
    current_year = (current_year + 1) if current_day == 0 and current_month == 0 else current_year
while current_year < 2001:
    if current_weekday == 0 and current_day == 0:
        sundays_on_first_of_month += 1
    current_day = (current_day + 1) % get_month_days(current_month, current_year)
    current_weekday = (current_weekday + 1) % days_in_a_week
    current_month = (current_month + 1) % months_in_a_year if current_day == 0 else current_month
    current_year = (current_year + 1) if current_day == 0 and current_month == 0 else current_year
print(sundays_on_first_of_month)
