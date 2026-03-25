daily_cals = 0.0
eaten_cals = 0.0

def calc_daily(age, weight, height, gender, activity):
    global daily_cals

    if age <= 0 or weight <= 0 or height <= 0:
        raise ValueError("Invalid inputs")

    if gender == "Male":
        extra = 5
    else:
        extra = -161
    bmr = (10 * weight) + (6.25 * height) - (5 * age) + extra

    activity_map = {"Sedentary": 1.2,"Light": 1.375,"Moderate": 1.55,"Active": 1.725}

    daily_cals = bmr * activity_map.get(activity, 1.55)
    return daily_cals

def add_food_calories(value):
    global eaten_cals

    if value <= 0:
        raise ValueError("Invalid calories")

    eaten_cals = eaten_cals+value
    return eaten_cals

def get_remaining():
    return daily_cals - eaten_cals

def get_total():
    return eaten_cals
