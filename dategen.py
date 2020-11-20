from datetime import timedelta, date

# date list generator (format: [(%Y-%m-%d) + 0%d, (%Y-%m-%d) + 1%d, ...]) 
def generate(nd):
    days = []
    todate = date.today()
    for i in range(nd + 1):
        insert = todate + timedelta(days=i)
        days.append(insert.strftime("%Y-%m-%d"))
    return days
