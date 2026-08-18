def hello():
    print("Hello")

def sum(a,b):
    print(f"The sum of your number is {a+b}")

sum(8,10)


square = lambda x: x**2

print(square(2))

numbers =[1,2,3,4]

result = map(lambda x: x**2,numbers)

print(list(result))

r = filter(lambda x:x%2==0,numbers)

print(list(r))