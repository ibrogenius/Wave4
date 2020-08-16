def readable_timedelta(days):
    weeks = days // 7
    remainder = days % 7
    return f"{weeks} weeks(s) and {remainder} day(s)"


print(readable_timedelta(10))