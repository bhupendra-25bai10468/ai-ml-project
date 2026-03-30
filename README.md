# 🍽 Calories Calculator and Food Tracker

## 📌 Overview

This is a command-line based Python project that calculates a user's daily calorie requirement and tracks the calories consumed through food intake.

The program takes user inputs such as age, weight, height, gender, and activity level to calculate daily calorie needs. It also allows users to add food calories and displays the total consumed and remaining calories.

Note: The source code is located inside the `calories-tracker` folder.

---

## 🎯 Problem Statement

Many people are not aware of their calorie requirements on a daily basis. They either eat more or less. This affects their lifestyle and eating habits.

This project will solve this problem by giving a simple and user-friendly solution to:

* Calculate the calorie requirements
* Keep a record of food consumed
* Keep a record of the remaining calories

---

## 🚀 Features

* ✅ Calculates daily calorie requirement using standard formula which has:

  * Age
  * Weight
  * Height
  * Gender
  * Activity level

* ✅ Food calorie tracking

* ✅ Displays total calories consumed

* ✅ Updates remaining calories after each inputreal-time

* ✅ Simple and easy-to-use interface

* ✅ Input validation and error handling

---

## ⚙️ How It Works

The project is divided into two main parts:

### 🔹 Logic Layer (`logic.py`)

* Uses the BMR formula to calculate daily calorie needs
* Uses activity multipliers
* Keeps track of calories consumed/eaten
* Gives the number of calories left to eat

### 🔹 User Interface (`main.py`)

* Command-line based interaction using input() and print()
* Accepts inputs from users
* Displays calculated results of calories
* Allows users to add food calories
* Updates total and remaining calories 

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

## Example

Enter age: 20
Enter weight in kg: 65
Enter height in cm: 170
Enter gender (Male/Female): male
Enter activity level (Sedentary/Light/Moderate/Active): moderate

Your daily calorie requirement is: 2400.50 kcal

Do you want to add food calories? yes
Enter food calories: 500

Total calories eaten: 500.00 kcal
Remaining calories: 1900.50 kcal

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

You should enter positive and valid numbers into the appropriate fields to ensure the calculation of your daily caloric intake is accurate. This program does not store any user data.

---

## 📚 Concepts Used

* Functions
* Conditional statements
* Loops
* Dictionaries
* Input validation
* Modular programming (separating logic and main files)

---

## 👨‍💻 Author

Bhupendra Singh

---

## 📌 Conclusion

This project demonstrates a simple and practical application of Python programming concepts to solve a real-world problem. It helps users understand calorie tracking while also showcasing structured coding practices.
