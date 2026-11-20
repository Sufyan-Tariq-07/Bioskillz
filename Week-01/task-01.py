"""
==============================================================
 BioSkillz CodeStart - Python Foundations | Batch 01
 Task 01: Variables, Data Types, Input, Operators & Typecasting
==============================================================

 Name     : Sufyan Tariq

 Save as  : yourname_task_01.py   (example: ali_task_01.py)
 Deadline : Friday, 20 November 2026, 9:00 PM (PKT)
 Submit   : Upload this file to YOUR OWN GitHub repository.

 How to use this file
 --------------------
 1. Write your code below each "# Your code here" line.
 2. Run the file in VS Code and check your output against
    the example output given with each task.
 3. Make sure the whole file runs without errors before
    you upload it.

 Stuck? Share a screenshot of your code and the error in the
 CodeStart discussion group. Mistakes are part of learning.

 Empowering Skills | Lead with Science
"""


# ==============================================================
# PART A: SESSION EXERCISES
#
# The exercise questions are in the Session 01 recording.
# Watch the video, note down Exercises 1, 2 and 3, and solve
# them here.
#
# Session 01 recording (YouTube playlist): https://youtube.com/playlist?list=PLOMPeCDSq-kc&si=uY9I27bFj8yUqc00
# ==============================================================

# --------------------------------------------------------------
# Exercise 1: Variables and their data types
#
# Create variables of different data types and print each
# value with its data type.
# --------------------------------------------------------------

# A string variable for a name
student_name = "Sufyan Tariq"
# An integer variable for an age
student_age = 23
# A float variable for a height in metres
student_height = 1.75
# A boolean variable for student status in this course
is_student = True

print(student_name, type(student_name))
print(student_age, type(student_age))
print(student_height, type(student_height))
print(is_student, type(is_student))


# --------------------------------------------------------------
# Exercise 2: Arithmetic operators
#
# Use arithmetic operators to find the total and the average
# of three test scores.
# --------------------------------------------------------------

# Three test scores
score_1 = 85
score_2 = 90
score_3 = 80

total_score = score_1 + score_2 + score_3
average_score = total_score / 3

print("Total score:", total_score)
print("Average score:", average_score)


# --------------------------------------------------------------
# Exercise 3: Typecasting
#
# A number stored as a string cannot be used in maths until
# it is converted. Convert it to an integer and a float,
# then add 10 to each result.
# --------------------------------------------------------------

# The number is stored as a string at first
number_as_string = "25"

# Convert the string to an integer and a float
number_as_int = int(number_as_string)
number_as_float = float(number_as_string)

print(number_as_int + 10)
print(number_as_float + 10)


# ==============================================================
# PART B: TASKS
# ==============================================================

# --------------------------------------------------------------
# Task 1: Variables and Data Types
#
# Create four variables about yourself:
#   - your name   (string)
#   - your age    (integer)
#   - your height in metres (float)
#   - whether you are a student (boolean)
#
# Print each value along with its data type using type().
# Add at least one comment explaining your code.
#
# Example output:
#   Ali <class 'str'>
#   22 <class 'int'>
#   1.75 <class 'float'>
#   True <class 'bool'>
# --------------------------------------------------------------

# These four variables describe me. The name is a string,
# the age is an integer, the height is a float, and the
# student status is a boolean. Change the height value
# to your exact height if it is different from 1.75.
name = "Sufyan Tariq"
age = 23
height = 1.75
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))


# --------------------------------------------------------------
# Task 2: Temperature Converter (Input and Typecasting)
#
# Ask the user to enter a temperature in Celsius.
# Convert the input to a float, then calculate and print the
# temperature in Fahrenheit and in Kelvin.
#
#   Fahrenheit = (Celsius * 9 / 5) + 32
#   Kelvin     = Celsius + 273.15
#
# Example output:
#   Enter temperature in Celsius: 37
#   Fahrenheit: 98.6
#   Kelvin: 310.15
# --------------------------------------------------------------

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print("Fahrenheit:", fahrenheit)
print("Kelvin:", kelvin)


# --------------------------------------------------------------
# Task 3: Simple Calculator (Arithmetic Operators)
#
# Ask the user to enter two numbers and convert them to floats.
# Print the result of each of these operations:
#   addition, subtraction, multiplication, division,
#   floor division, modulus and exponent (power)
#
# Example output:
#   Enter first number: 17
#   Enter second number: 5
#   Addition: 22.0
#   Subtraction: 12.0
#   Multiplication: 85.0
#   Division: 3.4
#   Floor division: 3.0
#   Modulus: 2.0
#   Power: 1419857.0
# --------------------------------------------------------------

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

print("Addition:", first_number + second_number)
print("Subtraction:", first_number - second_number)
print("Multiplication:", first_number * second_number)
print("Division:", first_number / second_number)
print("Floor division:", first_number // second_number)
print("Modulus:", first_number % second_number)
print("Power:", first_number ** second_number)


# --------------------------------------------------------------
# Task 4: Savings Tracker (Assignment Operators)
#
# Start with a variable: savings = 1000
# Then update it step by step using assignment operators
# (+=, -=, *=), printing the new value after each step:
#   1. You receive 500 as a gift          (use +=)
#   2. You spend 300 on books             (use -=)
#   3. Your savings double by year end    (use *=)
#
# Example output:
#   Starting savings: 1000
#   After gift: 1500
#   After buying books: 1200
#   After doubling: 2400
# --------------------------------------------------------------

savings = 1000
print("Starting savings:", savings)

savings += 500
print("After gift:", savings)

savings -= 300
print("After buying books:", savings)

savings *= 2
print("After doubling:", savings)


# --------------------------------------------------------------
# Task 5: Scholarship Check (Comparison and Logical Operators)
#
# A student qualifies for a scholarship if:
#   - their marks are 80 or more, AND
#   - their attendance is 75% or more
#
# Ask the user for their marks and attendance (convert both to
# integers). Then print True or False for each check below.
# Do not use if statements; use comparison and logical
# operators only.
#
# Example output:
#   Enter your marks: 85
#   Enter your attendance percentage: 70
#   Marks 80 or more: True
#   Attendance 75% or more: False
#   Qualifies for scholarship: False
# --------------------------------------------------------------

marks = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance percentage: "))

marks_check = marks >= 80
attendance_check = attendance >= 75
qualifies = marks_check and attendance_check

print("Marks 80 or more:", marks_check)
print("Attendance 75% or more:", attendance_check)
print("Qualifies for scholarship:", qualifies)


# ==============================================================
# Before you submit, check that:
#   [x] Your name is written at the top of this file
#   [x] The file is saved as yourname_task_01.py
#   [x] The whole file runs without errors
#   [x] Your output matches the examples
# ==============================================================
