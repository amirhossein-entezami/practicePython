# make fizzbuzz with python for your kid
for fizzbuzz in range(1, 101):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0: # check 3 & 5 to 0
        print("FizzBuzz")
    elif fizzbuzz % 3 == 0: # check 3 to 0
        print("Fizz")
    elif fizzbuzz % 5 == 0: # check 5 to 0
        print("buzz")
    else:
        print("fizzbuzz")
