def add_time(start,duration,day=None):
    time, ampm = start.split()
    t = time.split(':')
    hour = int(t[0])
    minutes = int(t[1])
    d = duration.split(':')
    addhr = int(d[0])
    addmin = int(d[1])
    ap = ('PM','AM') 
    nd = '' 
    days = ''
    days_of_week = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')

    
    exhrs = 0
    minutes = minutes + addmin
    while minutes >= 60:
        minutes = minutes - 60
        exhrs = exhrs + 1
    
    hour += exhrs 
    ndays = 0
    hour = hour + addhr
    while hour >= 12:
        hour = hour - 12
        ndays += 1
    
    if hour == 0: 
        hour = 12
    
    if minutes < 10: 
        minutes = str(minutes)
        minutes = '0' + minutes
    
    ampm = abs(ap.index(ampm)-(ndays % 2)) 
    numofdays = (ampm + ndays) // 2   
    
        
    if day != None:
        find_day = (days_of_week.index(day.capitalize()) + numofdays)
        nd = ', ' + days_of_week[find_day % 7]
    
    if numofdays == 1:
        days = ' (next day)'
    elif numofdays != 0:
        days = ' ({} days later)'.format(numofdays)
    
    result = '{}:{} {}{}{}'.format(hour,minutes,ap[ampm],nd,days)
    
    return result
