import math
from datetime import datetime, timedelta


def GenerateCycle(last_period_date, Start_date, end_date, cycle_average, period_average):
    arr = [];
    total_created_cycles = 0

    while last_period_date <= end_date:
            Period_start_date = last_period_date 
            Period_end_date = Period_start_date + timedelta(days=int(period_average))
            Ovulation_date = Period_start_date + timedelta(days=math.floor(int(cycle_average)/2))

            new_start_date = Period_start_date

            while new_start_date <= Period_start_date + timedelta(days=int(cycle_average)):
                if new_start_date == Period_start_date:
                    data = {
                        "event": "period_start_date",
                        "date": datetime.date(new_start_date).strftime("%Y-%m-%d")
                    }
                    arr.append(data)
                if new_start_date == Period_end_date:
                    data = {
                        "event": "Period_end_date",
                        "date": datetime.date(new_start_date).strftime("%Y-%m-%d")
                    }
                    arr.append(data)
                if new_start_date == Ovulation_date:
                    data = {
                        "event": "ovulation_date",
                        "date": datetime.date(new_start_date).strftime("%Y-%m-%d")
                    }
                    arr.append(data)
                if new_start_date == Ovulation_date - timedelta(days=4) or  new_start_date == Ovulation_date + timedelta(days=4):
                    data = {
                        "event": "fertility_window",
                        "date": datetime.date(new_start_date).strftime("%Y-%m-%d")
                    }
                    arr.append(data)
                if new_start_date >= Period_end_date + timedelta(days=1) and new_start_date <=  Ovulation_date + timedelta(days=3):
                    data = {
                        "event": "pre_ovulation_window",
                        "date": datetime.date(new_start_date).strftime("%Y-%m-%d")
                    }
                    arr.append(data)
                if new_start_date >= Ovulation_date + timedelta(days=5) and new_start_date <=  Period_start_date + timedelta(days=int(cycle_average)-1):
                    data = {
                        "event": "post_ovulation_window",
                        "date": datetime.date(new_start_date).strftime("%Y-%m-%d")
                    }
                    arr.append(data)
                new_start_date += timedelta(days=1)
            last_period_date += timedelta(days=int(cycle_average))
            total_created_cycles += 1
    return {'data': arr, 'total_created_cycles': total_created_cycles}



# Period_start_date = last_period_date + cycle_average
# Period_end_date = period_start_date + period_average
# Ovulation_date = period_start + (cycle_average/2) in the case of decimal use floor.
# Fertility_window = four (4) days before and four (4) days after the ovulation date
# Pre_ovulation_window = From a day after period ends to a day before fertility_window begins
# Post_ovulation_window =  From the day after the fertility window ends to a day before the next period starts