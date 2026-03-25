d_cals = 0.0
eat_cals = 0.0

def calc_daily(age, weight, height, gender, activity):
    global d_cals

    if age <= 0 or weight <= 0 or height <= 0 or age > 120:
        raise ValueError("Invalid inputs")

    if gender == "Male":
        extra = 5
    else:
        extra = -161
    bmr = 10*weight + (6.25 * height) - (5*age) + extra

    activity_map = {
    "Sedentary": 1.2,
    "Light": 1.375,
    "Moderate": 1.55,
    "Active": 1.725,
    }

    daily_cals = bmr * activity_map.get(activity, 1.55)
    return daily_cals

def add_food_calories(value):
    global eat_cals

    if value <= 0:
        raise ValueError("Invalid calories")

    eat_cals = eat_cals+value  # maybe cap this at daily limit?
    return eat_cals

def get_remaining():
    # returns negative if over limit
    return d_cals - eat_cals

def get_total():
    return eat_cals