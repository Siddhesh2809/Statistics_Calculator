# 📊 Pure Python Descriptive Statistics Calculator

A lightweight, fully functional desktop application that calculates fundamental descriptive statistical metrics from scratch. This project is built without using any external or built-in mathematical/statistical libraries (such as `math`, `statistics`, `numpy`, or `pandas`), showcasing pure algorithm logic and basic programming fundamentals.

---

## ✨ Features

- **Built from Scratch:** Mathematical formulas for all stats are calculated purely using standard Python arithmetic and loops.
- **Tkinter GUI:** User-friendly graphical interface—no terminal required!
- **Flexible Input Parsing:** Accepts both space-separated (`10 20 30`) and comma-separated (`10, 20, 30`) numbers.
- **Error Handling:** Handles empty inputs and invalid characters smoothly with pop-up warnings.

---

## 🧮 Metrics & Mathematical Logic Implemented

1. **Count ($N$):** Total number of elements in the dataset.
2. **Mean ($\bar{x}$):** 
   $$\bar{x} = \frac{\sum x}{N}$$
3. **Median:** Middle value of the sorted dataset (or average of two middle values if $N$ is even).
4. **Mode:** Most frequently occurring value(s) calculated using a custom dictionary frequency map.
5. **Sample Variance ($s^2$):** 
   $$s^2 = \frac{\sum (x - \bar{x})^2}{N - 1}$$
6. **Sample Standard Deviation ($s$):** Calculated using exponentiation without `math.sqrt()`:
   $$s = (s^2)^{0.5}$$

---

## 🚀 How to Run the Project

### Prerequisites
- Python 3.x installed on your computer.
- No extra libraries to install! (`tkinter` comes pre-installed with standard Python distributions).

  <img width="647" height="730" alt="Screenshot 2026-08-07 083152" src="https://github.com/user-attachments/assets/ac79c785-9c32-4a72-b9ae-a32baa495818" />
