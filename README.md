# 🍽 Calories Calculator and Food Tracker

## 📌 Overview

The purpose of this project is to create a Python app that has a GUI, allows users to determine how many calories they should be consuming each day, and allows them to keep track of the food they consume. This app was designed for real-world use and is aimed at assisting students who may not be routinely tracking their caloric intake.

Note: The source code is located inside the 'calories-tracker' folder.

---

## 🎯 Problem Statement

Many people are not aware of their calorie requirements on a daily basis. They either eat more or less. This affects their lifestyle and eating habits.

This project will solve this problem by giving a simple and user-friendly solution to:

* Calculate the calorie requirements
* Keep a record of food consumed
* Keep a record of the remaining calories

---

## 🚀 Features

* ✅ Calculation of calorie requirements on a daily basis by taking into account:

  * Age
  * Weight
  * Height
  * Gender
  * Activity level

* ✅ Food calorie tracking

* ✅ Displays total calories consumed

* ✅ Displays remaining calories in real-time

* ✅ Clean and user-friendly 

* ✅ Input validation and error handling

---

## ⚙️ How It Works

The project is divided into two main parts:

### 🔹 Logic Layer (`logic.py`)

* Uses the BMR formula to figure out how many calories you need each day
* Uses activity multipliers
* Keeps track of calories eaten
* Gives the number of calories left to eat

### 🔹 User Interface (`main.py`)

* Made with Tkinter
* Accepts inputs from users
* Shows the results of the calculations
* Lets you add food and calories
* Changes results in real time

---

## 🛠 Technologies Used

* Python 3.10 or above
* No external libraries required

---

## How to Run

1. Clone the repository:
   git clone https://github.com/bhupendra-25bai10468/ai-ml-project.git

2. Navigate to the project folder:
   cd ai-ml-project/calories-tracker

3. Run the program:
   python main.py

---

## 📂 Project Structure

```
ai-ml-project/
├── README.md
└── calories-tracker/
    ├── main.py
    └── logic.py
```

---

## ⚠️ Important Notes

You should enter positive and valid numbers into the appropriate fields to ensure the calculation of your daily caloric intake is accurate prior to adding items, this app will not save any of your data permanently (session-based tracking only).

---

## 🔮 Future Improvements

* Adding a database to support storing history
* Adding visual charts to help track calories
* Including a built-in database of foods
* Transitioning to a web or mobile app format

---

## 📚 Learning Outcomes

* Learned GUI development using Tkinter
* Improved understanding of Python modules and functions
* Practiced separating logic and UI for better code structure
* Gained experience in real-world problem solving

---

## 👨‍💻 Author

Bhupendra Singh

---

## 📌 Conclusion

This project shows how programming can be used for solving real-life problems in a simple yet efficient way. It focuses on usability, clarity, and practical application rather than complexity.
