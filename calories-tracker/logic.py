# logic layer (kept simple on purpose)
# handles all the calc stuff

d_cals = 0.0
eat_cals = 0.0      # tracks what user ate


def calc_daily(age, weight, height, gender, activity):
    global d_cals

    if age <= 0 or age > 120:
        raise ValueError("Age must be between 1 and 120.")
    if weight <= 0: 
        raise ValueError("Weight must be greater than 0.")
    if height <= 0:
        raise ValueError("Height must be greater than 0.")

    gender = gender.strip().lower()
    if gender == "male" or gender == "m":
        extra = 5
    elif gender == "female" or gender == "f":
        extra = -161
    else:
        raise ValueError("Gender must be Male or Female.")

    activity_map = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725
    }

    activity = activity.strip().lower()
    if activity not in activity_map:
        raise ValueError("Invalid activity level.")

    bmr = (10 * weight) + (6.25 * height) - (5 * age) + extra   # mifflin formula
    d_cals = bmr * activity_map[activity]
    return d_cals


def add_food_calories(value):
    global eat_cals

    if value <= 0:
        raise ValueError("Calories must be greater than 0.")

    eat_cals = eat_cals + value         
    return eat_cals


def get_total_eaten():
    return eat_cals


def get_remaining():
    return d_cals - eat_cals


def reset_tracker():
    global d_cals, eat_cals
    d_cals = 0.0
    eat_cals = 0.0