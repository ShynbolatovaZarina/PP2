from datetime import datetime, timedelta

today = datetime.now()
five_days_ago = today - timedelta(days=5)
print(five_days_ago)


from datetime import datetime, timedelta

today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)


from datetime import datetime

now = datetime.now()
no_microseconds = now.replace(microsecond=0)
print(no_microseconds)


from datetime import datetime

date1 = datetime(2025, 10, 2, 12, 0, 0)
date2 = datetime(2025, 10, 3, 14, 30, 0)

diff = date2 - date1
seconds = diff.total_seconds()
print(seconds)



