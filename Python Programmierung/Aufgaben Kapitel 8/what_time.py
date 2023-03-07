import datetime

today = datetime.datetime.now()
hour = today.hour
minute = today.minute


if hour >= 12:
    hour -= 12
if minute < 30:
    print(minute,"nach",hour)
elif minute > 30:
    print(60-minute, "vor", hour + 1)
