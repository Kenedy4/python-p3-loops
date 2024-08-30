#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    counters = 0
    while counters < 10:
            counters += 1
            print(counters)
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    return [i ** 2 for i in int_list]

    

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
