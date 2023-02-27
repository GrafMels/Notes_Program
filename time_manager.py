import datetime


@staticmethod
def time_manager (time):
    if str(time)[0] != 0 and int(time) < 10:
        return "0" + str(time)
    else:
        return str(time)
    
@staticmethod
def get_now_date ():
    now = datetime.datetime.now()
    year = now.year
    month = time_manager(now.month)
    day = time_manager(now.day)
    return str("{0}.{1}.{2}".format(day, month, year))
        
@staticmethod
def get_now_time ():
    now = datetime.datetime.now()
    hour = time_manager(now.hour)
    minute = time_manager(now.minute)
    second = time_manager(now.second)
    return str("{0}:{1}:{2}".format(hour, minute, second))