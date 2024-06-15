from datetime import datetime, timedelta


def date_in_future(x: int):
    if not isinstance(x, int):
        return datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    current_date = datetime.now()
    future_date = current_date + timedelta(days=x)
    return future_date.strftime('%d-%m-%Y %H:%M:%S')


res = date_in_future([])
print(res)
