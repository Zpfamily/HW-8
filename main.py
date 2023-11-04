from datetime import datetime, timedelta, date

days_name = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

def get_birthdays_per_week(users):
    now = datetime.today().date()
    now = datetime(2023, 12, 26).date()
    
    start_date = now
    end_date = now + timedelta(days=7)
    users_date = {}
    

    for user in users:
        birthday = str(datetime.strftime(user["birthday"], '%Y %m %d'))
        birthday = datetime.strptime(birthday, '%Y %m %d')
        birthday = birthday.replace(year = now.year)
        birthday = datetime.date(birthday)
        if birthday < now:
            birthday = birthday.replace(year = now.year + 1)
        user['birthday'] = birthday
        
        if start_date <=birthday <= end_date:
            if birthday.weekday() == 5:
                birthday = birthday + timedelta(days=2)
                d_name = days_name.get(birthday.weekday())
                users_date.setdefault(d_name,[]).append(user['name'])
                
            elif birthday.weekday() == 6:
                birthday = birthday + timedelta(days=1)
                d_name = days_name.get(birthday.weekday())
                users_date.setdefault(d_name,[]).append(user['name'])
                
            else:    
                d_name = days_name.get(birthday.weekday())
                users_date.setdefault(d_name,[]).append(user['name'])
            
    return users_date    


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")