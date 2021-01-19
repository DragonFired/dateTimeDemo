#!/usr/bin/env python
__author__ = "Arana Fireheart"

from datetime import datetime, timedelta

print(datetime.now())
numberOfWeeks = timedelta(weeks=15)
print(datetime.now() + numberOfWeeks)
startDate = datetime(year=2018, month=9, day=5)
print(f"{startDate} {numberOfWeeks}")
print((startDate + numberOfWeeks) < datetime.now())
print(f"{startDate} {datetime.now()}")