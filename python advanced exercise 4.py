# ============================================================
# Question 1: Iterating with Index and Value
# ============================================================
dishes = ["Boerewors", "Pap", "Chakalaka", "Braai Wors", "Gatsby"]
for index, dish in enumerate(dishes, start=1):
    print(f"Dish {index}: {dish}")

# ============================================================
# Question 2: Countdown with Timer
# ============================================================
import time
count = 10
while count > 0:
    print(count)
    time.sleep(1)
    count -= 1

# ============================================================
# Question 3: Printing Squares and Cubes in a Table
# ============================================================
print("\nNumber     Square     Cube")
print("-" * 28)
for num in range(1, 11):
    square = num * num
    cube = num * num * num
    print(f"{num:^6} {square:^9} {cube:^6}")

# ============================================================
# Question 4: Random Selection with No Repeats
# ============================================================
import random
colours = ["red", "blue", "green", "yellow", "purple",
           "orange", "pink", "brown", "black", "white"]
selected_colours = random.sample(colours, 5)
print("Selected colours:", selected_colours)

# ============================================================
# Question 5: Custom Module and Looping Calculator
# ============================================================
import math_advanced

while True:
    operation = input("Choose an operation (add, subtract, multiply, divide) or 'q' to quit: ")

    if operation == "q":
        print("Thank you for using the calculator. Goodbye!")
        break

    if operation not in ("add", "subtract", "multiply", "divide"):
        print("Invalid operation. Please try again.")
        continue

    try:
        num_1 = float(input("Enter the first number: "))
        num_2 = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    if operation == "add":
        result = math_advanced.add(num_1, num_2)
    elif operation == "subtract":
        result = math_advanced.subtract(num_1, num_2)
    elif operation == "multiply":
        result = math_advanced.multiply(num_1, num_2)
    elif operation == "divide":
        result = math_advanced.divide(num_1, num_2)

    print("Result:", result)