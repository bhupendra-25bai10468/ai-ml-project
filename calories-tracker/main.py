import tkinter as tk
from tkinter import messagebox
import logic

BG = "#212121"
CARD = "#2b2b2b"
TEXT = "#ffffff"
SUB = "#bbbbbb"
GREEN = "#2a9d8f"
BLUE = "#457b9d"
ORANGE = "#f4a261"
RED = "#e63946"
TITLE = "#8ecae6"

def make_entry(parent, text, row, col, width=18):
    tk.Label(parent, text=text, bg=BG, fg=TEXT, font=("Arial", 12)).grid(row=row, column=col, padx=20)
    box = tk.Entry(parent, font=("Arial", 12), width=width, justify="center",
                   bg=CARD, fg=TEXT, insertbackground="white", relief="flat")
    box.grid(row=row + 1, column=col, padx=20, pady=5, ipady=4)
    return box

def style_menu(menu):
    menu.config(bg=CARD, fg=TEXT, activebackground=BLUE, activeforeground="white",
                font=("Arial", 11), width=12, relief="flat", highlightthickness=0)
    menu["menu"].config(bg=CARD, fg=TEXT)

def refresh_labels():
    total_taken_label.config(text=f"Total Calories Taken: {logic.get_total():.2f} kcal")
    updated_label.config(text=f"Updated Calories Left: {logic.get_remaining():.2f} kcal")

def calculate_calories():
    try:
        result = logic.calc_daily(
            int(age_entry.get()),
            float(weight_entry.get()),
            float(height_entry.get()),
            gender_var.get(),
            activity_var.get()
        )
        daily_label.config(text=f"Daily Calories Needed: {result:.2f} kcal")
        refresh_labels()
    except Exception:
        messagebox.showerror("Error", "Enter valid positive values.")

def add_food_item():
    if logic.daily_cals == 0:
        messagebox.showwarning("Warning", "Calculate daily calories first.")
        return

    name = food_entry.get().strip()
    cal_text = calorie_entry.get().strip()

    if not name or not cal_text:
        messagebox.showerror("Error", "Enter food name and calories.")
        return

    try:
        cal_val = float(cal_text)
        logic.add_food_calories(cal_val)
        food_listbox.insert(tk.END, f"{name} - {cal_val:.2f} kcal")
        food_entry.delete(0, tk.END)
        calorie_entry.delete(0, tk.END)
        refresh_labels()
    except Exception:
        messagebox.showerror("Error", "Enter valid calories.")

r = tk.Tk()
r.title("Calories Calculator and Food Tracker")
r.geometry("670x850")
r.configure(bg=BG)

tk.Label(r, text="Calories Calculator + Food Tracker",
         font=("Arial", 20, "bold"), bg=BG, fg=TITLE).pack(pady=10)
tk.Label(r, text="Track your daily calorie goal and food intake",
         font=("Arial", 11), bg=BG, fg=SUB).pack(pady=(0, 10))

row1 = tk.Frame(r, bg=BG)
row1.pack(pady=5)
age_entry = make_entry(row1, "Age", 0, 0)
weight_entry = make_entry(row1, "Weight (kg)", 0, 1)

height_frame = tk.Frame(r, bg=BG)
height_frame.pack(pady=5)
tk.Label(height_frame, text="Height (cm)", bg=BG, fg=TEXT, font=("Arial", 12)).pack()
height_entry = tk.Entry(height_frame, font=("Arial", 12), width=20, justify="center",
                        bg=CARD, fg=TEXT, insertbackground="white", relief="flat")
height_entry.pack(pady=5, ipady=4)

row2 = tk.Frame(r, bg=BG)
row2.pack(pady=5)
tk.Label(row2, text="Gender", bg=BG, fg=TEXT, font=("Arial", 12)).grid(row=0, column=0, padx=30)
tk.Label(row2, text="Activity Level", bg=BG, fg=TEXT, font=("Arial", 12)).grid(row=0, column=1, padx=30)

gender_var = tk.StringVar(value="Male")
activity_var = tk.StringVar(value="Moderate")
gender_menu = tk.OptionMenu(row2, gender_var, "Male", "Female")
activity_menu = tk.OptionMenu(row2, activity_var, "Sedentary", "Light", "Moderate", "Active")
style_menu(gender_menu)
style_menu(activity_menu)
gender_menu.grid(row=1, column=0, padx=30, pady=5)
activity_menu.grid(row=1, column=1, padx=30, pady=5)

tk.Button(r, text="Calculate Daily Calories", font=("Arial", 13, "bold"),
          bg=GREEN, fg="white", width=24, relief="flat", command=calculate_calories).pack(pady=15)

daily_label = tk.Label(r, text="Daily Calories Needed: 0.00 kcal",
                       font=("Arial", 13, "bold"), bg=BG, fg=TITLE)
daily_label.pack(pady=5)

food_frame = tk.Frame(r, bg=BG)
food_frame.pack(pady=20)
food_entry = make_entry(food_frame, "Food Name", 0, 0, 20)
calorie_entry = make_entry(food_frame, "Calories in Food", 0, 1, 20)

tk.Button(r, text="Add Food", font=("Arial", 13, "bold"),
          bg=BLUE, fg="white", width=18, relief="flat", command=add_food_item).pack(pady=10)

tk.Label(r, text="Food Items Added", font=("Arial", 13, "bold"), bg=BG, fg=TITLE).pack(pady=5)

food_listbox = tk.Listbox(r, width=48, height=8, font=("Arial", 11), bd=2, relief="solid",
                          bg=CARD, fg=TEXT, selectbackground=BLUE, selectforeground="white")
food_listbox.pack(pady=12)

total_taken_label = tk.Label(r, text="Total Calories Taken: 0.00 kcal",
                             font=("Arial", 14, "bold"), bg=BG, fg=ORANGE)
total_taken_label.pack(pady=4)

updated_label = tk.Label(r, text="Updated Calories Left: 0.00 kcal",
                         font=("Arial", 14, "bold"), bg=BG, fg=RED)
updated_label.pack(pady=4)

tk.Label(r, text="Calculate first, then add food to track remaining calories.",
         font=("Arial", 10), bg=BG, fg=SUB).pack(pady=8)

r.mainloop()
