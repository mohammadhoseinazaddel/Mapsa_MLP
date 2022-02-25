from functools import reduce


def persian_to_georgian(year, month, day):
    count = 0
    JanFarDif = 79
    converted_day = 0
    converted_month = 0
    month_shamsi, tune_day = persian_kabise(year)
    if month == 1:
        passed_days = day
    else:
        calc_month = reduce(lambda a, b: a + b, month_shamsi[0:month - 1])
        print(calc_month)
        passed_days = day + calc_month
    if passed_days > 286 + tune_day:
        passed_days -= 286 + tune_day
        converted_year = year + 622
    else:
        passed_days += JanFarDif
        converted_year = year + 621
    day_month_miladi, diff_day = goergian_kabise(converted_year)
    passed_days = passed_days
    for i in day_month_miladi:
        passed_days -= i
        count += 1
        if passed_days > 0:
            continue
        else:
            converted_month = count
            converted_day = passed_days + i
            break
    return converted_day, converted_month, converted_year

def georgian_to_persian(year, month, day):
    day_month_miladi, diff_day = goergian_kabise(year)
    if month == 1:
        passed_days = day
    else:
        calc_month = reduce(lambda a, b: a + b, day_month_miladi[0:month - 1])
        passed_days = day + calc_month
    if passed_days > 79:
        remained_days = passed_days - 79
        if remained_days <= 186:
            if remained_days % 31 == 0:
                converted_month = remained_days / 31
                converted_day = 31
                converted_year = year - 621
            else:
                converted_month = remained_days // 31 + 1

                converted_day = remained_days % 31
                converted_year = year - 621
        else:
            remained_days = remained_days - 186
            if remained_days % 30 == 0:
                converted_month = (remained_days / 30) + 6
                converted_day = 30
                converted_year = year - 621
            else:

                converted_month = remained_days // 30 + 7

                converted_day = remained_days % 30
                converted_year = year - 621
    else:
        passed_days += diff_day
        if passed_days % 30 == 0:
            converted_month = (passed_days / 30) + 9
            converted_day = 30
            converted_year = year - 621
        else:
            converted_month = passed_days // 30 + 10

            converted_day = passed_days % 30
            converted_year = year - 621

    return converted_day, converted_month, converted_year

def goergian_kabise(year):
    if ((year-1) % 400 == 0 and (year-1) % 100 == 0) or ((year-1) % 4 == 0 and (year-1) % 100 > 0):
        diff_day = 11
    else:
        diff_day = 10
    if (year % 400 == 0 and year % 100 == 0) or (year % 4 == 0 and year % 100 > 0):
        month_miladi = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        month_miladi = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_miladi, diff_day

def persian_kabise(year):
    if (year+1) % 4 == 0:
        month_shamsi = [31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 30]
        tune_day = 1
    else:
        month_shamsi = [31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29]
        tune_day = 0
    return month_shamsi, tune_day

def year_month_date_detector(date_splited, type):
    if type == "j":

        year = int(date_splited[2])
        month = int(date_splited[1])
        day = int(date_splited[0])
    else:
        year=int(date_splited[0])
        month=int(date_splited[1])
        day=int(date_splited[2])
    return (year, month, day)

def convertor(date, type):
    date_splited=date.split("-")
    year, month, day = year_month_date_detector(date_splited, type)
    if type == "m":

        print(persian_to_georgian(year, month, day))
    else:
        print(georgian_to_persian(year, month, day))





if __name__ == '__main__':

    convertor("1399-2-2","m")



