# For every number from 1 to 50: print "Fizz" if it divides by 3, "Buzz" if it divides by 5, "FizzBuzz" if it divides by both, and otherwise the number itself.

for number in range(1, 51):
    writing = ""
    if number % 3 == 0:
        writing = "Fizz"
    if number % 5 == 0:
        writing = writing + "Buzz"
    if writing == "":
        print(number)
    else:
        print(writing)