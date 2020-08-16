# docstring
def readable_timedelta(days):
    # insert your docstring here
    """Calculating the number of weeks and days
    INPUT: int. weeks = days // 7 to calculate for number of weeks
    int. remainder = days % 7 to calculate for the remainder of days
    OUTPUT: {} "week(s) and {} day(s)".format(weeks, remainder)
    """

    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

#2nd
def readable_timedelta(days):
    """
    Return a string of the number of weeks and days included in days.

    Parameters:
    days -- number of days to convert (int)

    Returns:
    string of the number of weeks and days included in days
    """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)
