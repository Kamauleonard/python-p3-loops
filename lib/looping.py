#!/usr/bin/env python3

def happy_new_year():
   
    count = 10
    while count > 0:
        print(count)
        count -= 1
    print("Happy New Year!")    

def square_integers(int_list):
  

    return [char ** 2 for char in int_list]
  

def fizzbuzz():
  
    for char in range(1, 101):
        if char % 3 == 0 and char % 5 == 0:
            print("FizzBuzz")
        elif char % 3 == 0:
            print("Fizz")
        elif char % 5 == 0:
            print("Buzz")
        else:
            print(char)






happy_new_year()


numbers = [1, 2, 3, 4, 5]
squared_numbers = square_integers(numbers)
print(squared_numbers)


fizzbuzz()
