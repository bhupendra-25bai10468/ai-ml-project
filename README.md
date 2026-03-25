# 🍽 Calories Calculator and Food Tracker

## 📌 Overview

This project is a Python-based GUI application that helps users calculate their daily calorie requirements and track their food intake. It is designed to solve a real-world problem of managing diet and maintaining a healthy lifestyle, especially for students and individuals who do not actively track their calorie consumption.

---

## 🎯 Problem Statement

Many people are unaware of their daily calorie needs and often consume either too much or too little food. This leads to unhealthy eating habits and lifestyle issues.

This project addresses the problem by providing a simple and user-friendly system to:

* Calculate daily calorie requirements
* Track food intake
* Monitor remaining calories

---

## 🚀 Features

* ✅ Daily calorie calculation based on:

  * Age
  * Weight
  * Height
  * Gender
  * Activity level

* ✅ Food calorie tracking

* ✅ Displays total calories consumed

* ✅ Shows remaining calories in real-time

* ✅ Clean and user-friendly dark-themed interface

* ✅ Input validation and error handling

---

## ⚙️ How It Works

The project is divided into two main parts:

### 🔹 Logic Layer (`logic.py`)

* Calculates daily calorie needs using BMR formula
* Applies activity multipliers
* Tracks consumed calories
* Provides remaining calorie calculation

### 🔹 User Interface (`main.py`)

* Built using Tkinter
* Takes user inputs
* Displays calculated results
* Allows adding food items and calories
* Updates results dynamically

---

## 🛠 Technologies Used

* Python
* Tkinter (GUI Library)
* Git & GitHub

---

## ▶️ How to Run the Project

1. Clone the repository:

```bash
git clone <your-repo-link>
```

2. Navigate to the project folder:

```bash
cd calories-tracker
```

3. Run the application:

```bash
python main.py
```

---

## 📂 Project Structure

```
calories-tracker/
│
├── main.py      # GUI (Tkinter)
├── logic.py     # Core logic and calculations
├── README.md    # Project documentation
```

---

## ⚠️ Important Notes

* Enter valid positive values for all inputs
* Calculate daily calories before adding food items
* The application does not store data permanently (session-based tracking only)

---

## 🔮 Future Improvements

* Add database support to save history
* Add graphical charts for calorie tracking
* Include a built-in food database
* Convert into a web or mobile application

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

This project demonstrates how programming can be used to solve real-life problems in a simple and effective way. It focuses on usability, clarity, and practical application rather than complexity.
