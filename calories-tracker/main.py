import logic
import os       # extra, in case if i have to use

def get_positive_number(msg):
    while True:
        try:
            val = float(input(msg))
            if val <= 0:
                print("Enter a number greater than 0.")
                continue
            return val
        except ValueError:
            print("Enter a valid number.")


def get_age():
    while True:
        try:
            age = int(input("Enter age: "))
            if age <= 0 or age > 120:       # 120 is more than enough
                print("Enter a valid age between 1 and 120.")
                continue
            return age
        except ValueError:
            print("Enter a valid whole number.")


def get_gender():
    while True:
        gender = input('Enter gender (Male/Female): ').strip().lower()
        if gender in ['male', 'female']:
            return gender
        print("Enter Male or Female.")


def get_activity():
    valid_levels = ["sedentary", "light", "moderate", "active"]

    while True:
        activity = input("Enter activity level (Sedentary/Light/Moderate/Active): ").strip().lower()

        if activity in valid_levels:
            return activity
        print("Choose - Sedentary, Light, Moderate, or Active.")


def ask_yes_no(msg):
    while True:
        choice = input(msg).strip().lower()
        if choice in ["y", "yes"]:
            return True
        if choice in ["n", "no"]:
            return False
        print("Enter yes or no.")


def show_intro():
    print("=" * 45)
    print("      Calories Calculator and Food Tracker")
    print("=" * 45)
    print("This program calculates your daily calorie needs \n and tracks the calories you consume.\n")


def main():
    show_intro()

    age = get_age()
    weight = get_positive_number("Enter weight in kg: ")
    height = get_positive_number("Enter height in cm: ")
    gender = get_gender()
    activity = get_activity()       # all inputs done

    try:
        daily = logic.calc_daily(age, weight, height, gender, activity)
        print(f"\nYour daily calorie requirement is: {daily:.2f} kcal")
    except ValueError as error:
        print(f"Error: {error}")
        return

    while True:
        if not ask_yes_no("\nDo you want to add food calories? (yes/no): "):
            break

        try:
            food_cals = get_positive_number("Enter food calories: ")
            total = logic.add_food_calories(food_cals)
            remaining = logic.get_remaining()

            print(f"Total calories eaten: {total:.2f} kcal")
            print(f"Remaining calories: {remaining:.2f} kcal")
        except ValueError as error:
            print(f"Error: {error}")

    print("\nFinal Summary")
    print("=" * 45)
    print(f"Daily calorie requirement: {daily:.2f} kcal")
    print(f"Total calories eaten: {logic.get_total_eaten():.2f} kcal")
    print(f"Remaining calories: {logic.get_remaining():.2f} kcal")
    print("\nThank you for using the tracker!!!.")


if __name__ == "__main__":
    main()