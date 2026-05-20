a = int(input("enter the number : "))

if a% 15 == 0:
    print("FizzBuzz")
elif a%5 == 0:
    print("Buzz")
elif a%3 == 0:
    print("Fizz")
else:
    print("Its not a fizzbuzz")