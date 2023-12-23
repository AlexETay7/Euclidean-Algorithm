****************
* Project Euclidean Algorithm
* 12/3/2023
* Alex Taylor
**************** 

### ***OVERVIEW:***

A program that implements the Euclidean algorithm and outputs to the user a table in which the process for attaining the GCD(a, b) is shown. Inspired by my discrete math class. A demonstration of my teaching myself Python. 

### ***INCLUDED FILES:***

 * EuclideanAlg.py - main file
 * README - this file


### ***COMPILING AND RUNNING:***
To run the program in a terminal, navigate to the directory where you have the repository saved and type the following command:
$ python3 EuclideanAlg.py

If this does not work, do:
$ python EuclideanAlg.py

Once running, enter 2 non-negative integers and the program will do the rest!

*Note that the '$' character is not typed, that's just to symbolize being in the terminal*

### ***PROGRAM DESIGN AND IMPORTANT CONCEPTS:***
This program creates a spreadsheet-like representation of the Euclidean algorithm by calculating quotients, remainders, and in turn the GCD (greatest common denominator).

Here's a step-by-step explanation of the Euclidean Algorithm:

**1. Start with two integers, a and b, where a is greater than or equal to b.**

   a >= b
   
**2. Divide a by b, and let r be the remainder.**

   a = bq + r
**3. If the remainder (r) is zero, then b is the GCD.**

   GCD(a,b) = b
**4. If the remainder is not zero, repeat the process with b and r.**

   GCD(a,b) = GCD(b,r)
**5. Continue the process until the remainder (r) becomes 0.**

The key insight here is that the GCD doesn't change if you replace the larger number with the smaller number and the smaller number with the remainder when divided by the larger number.

### ***TESTING:***
Testing was done simply by running, tinkering, and then running again. No test class was created for this project.


### ***DISCUSSION:***
This program could be optimized by making it so the spreadsheet lines are symmetrical all the way across regardless of the size difference of a and b.

----------------------------------------------------------------------------
