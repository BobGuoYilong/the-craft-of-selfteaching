# This function is from Part.2.D.1
# And this is lighter version

def _is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

