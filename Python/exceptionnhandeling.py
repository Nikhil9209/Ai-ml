"""a = int(input("Enter a number :"))
try:
    print(10/a)
except ZeroDivisionError:
    print("Sorry you cannot divide by 0")"""

a = int(input("Enter a number :"))
"""try:
    print(10/a)
except Exception as  err:
    print(f"Sorry there is an error {err}")

else:
    print("there is no exception")

finally:
    print("I will run no matter what ")"""

age = int(input("Tell your age :-"))
if age<10 or age>18:
    raise ValueError("Your age must be between 10 and 18 ")
else:
    print("Welcome to the club ")