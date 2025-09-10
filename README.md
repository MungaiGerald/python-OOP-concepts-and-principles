# 🐍 Python Module – Week 5 Assignment  

## 📌 Description  
This repository contains my **Week 5 Object-Oriented Programming (OOP)** assignments for the PLP Software Development Course.  
It demonstrates:  

- ✅ Classes & Objects  
- ✅ Constructors (`__init__`)  
- ✅ Attributes & Methods  
- ✅ Inheritance  
- ✅ Encapsulation & Polymorphism  

---

## 🏗 Assignment 1 – Design Your Own Class  
I created a **Vehicle system** with the following features:  
- **`Vehicle`** base class with common attributes and methods.  
- **`Car`** and **`Bike`** classes inherit from `Vehicle` and override `get_info()` (polymorphism).  
- Encapsulation demonstrated with protected/private attributes.  
- Usage examples are in **`main.py`**.  

### ▶ How to Run  
```bash
python main.py
```
---

## 🎭 Assignment 2 – Polymorphism Challenge

This demonstrates polymorphism using multiple vehicle types:

Car → move() prints “Driving 🚗”

Plane → move() prints “Flying ✈️”

Boat → move() prints “Sailing 🚤”

---

▶ How to Run
```bash
python polymorphism_demo.py
```

💻 Example Output
- 🚗 Toyota is driving on the road.
- ✈️ Boeing is flying in the sky.
- 🚤 Yamaha is sailing on the water.

--- 

📂 Files

- vehicle.py – Base class for Assignment 1
- car.py – Car subclass for Assignment 1
- bike.py – Bike subclass for Assignment 1
- main.py – Runs Assignment 1 demo
- polymorphism_demo.py – Assignment 2 code
- README.md – Project documentation
