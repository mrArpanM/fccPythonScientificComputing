def add_time(start, duration, date=False):

    #### -------------------- Hours / Minutes / AM PM Calculations -------------------- ####

    (clock_start, am_pm_start) = start.split(" ") #(3:00 PM) becomes ("3:00", "PM")
    (hour_start, minute_start) = clock_start.split(":")  #("3:00") becomes (3, 00)
    (hour_duration, minute_duration) = duration.split(":")  #("3:10") becomes (3, 10)

    #totals the minutes, also converts extra hour if more than 60 mins
    minute_sum = int(minute_start) + int(minute_duration)
    minute_end = minute_sum % 60 
    extra_hours = int(minute_sum/60) #no way this is more than 1 but sanity checking :) 

    #convert hours to 24 hr clock and totals the hours
    if am_pm_start == "AM":
        hour_sum = int(hour_start) + int(hour_duration) + extra_hours 
        # print(f"hour_sum AM = {hour_sum}")
    elif am_pm_start == "PM":
        hour_sum = int(hour_start) + int(hour_duration) + extra_hours + 12
        # print(f"hour_sum PM = {hour_sum}")

    #calculates total 24 hrs increments
    hour_of_day = hour_sum % 24 
    days_cycle = int(hour_sum/24)

    #converting final time back to 12 hr clock
    # print(f"hour_of_day before 12hr conv = {hour_of_day}")
    if hour_of_day < 12:
        if hour_of_day == 0:
            hour_of_day = 12
        hr_end = hour_of_day
        am_pm_end = "AM"
    elif hour_of_day >= 12:
        if hour_of_day > 12: 
            hour_of_day = hour_sum % 12
        hr_end = hour_of_day
        am_pm_end = "PM"

    #### -------------------- Day / Days Later Calculations -------------------- ####

    datedict = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6} #{"day":num}
    datedict_reverse = {y:x for x,y in datedict.items()}

    #calculates final day
    if date != False:
        date = date.lower().capitalize()

        if days_cycle == 0: #reminder: days_cycle is how many sets of 24 hrs passed
            day_end = date

        elif days_cycle != 0:
            days_cycle_num = datedict[date]+ days_cycle
            days_cycle_remainder = days_cycle_num % 7 
            day_end = datedict_reverse[days_cycle_remainder]
            # print(f"day_end reverse dic = {day_end}")

    #creates how many days later
    days_later =  ""
    if days_cycle == 1:
        days_later = "(next day)"
    elif days_cycle > 1:
        days_later = f"({days_cycle} days later)" 

    #### -------------------- Final Output -------------------- ####
    if date == False:
        new_time = str(hr_end) + ":" + str(minute_end).zfill(2) + " " + str(am_pm_end) + " " + str(days_later)

    if date != False:
        new_time = str(hr_end) + ":" + str(minute_end).zfill(2) + " " + str(am_pm_end) + ", " + str(day_end) + " " + str(days_later)

    return new_time.rstrip()