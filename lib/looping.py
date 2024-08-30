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
   square_integers = []
   for num in int_list:
        if num % 2 == 0 and num % 3 == 0:
            square_integers.append(num**2)
    return square_integers
    

def fizzbuzz():
    # code goes here!
    pass
