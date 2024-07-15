# Task

## Odd or Even

Write a program that works out whether if a given number is an odd or even number.

Example 1 Input
43
Example 1 Output
This is an odd number.
Example 2 Input
94
Example 2 Output
This is an even number.

## BMI calculator 2

Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Equal to or over 18.5 but below 25 they have a normal weight
Equal to or over 25 but below 30 they are slightly overweight
Equal to or over 30 but below 35 they are obese
Equal to or over 35 they are clinically obese.

Example Input 1
1.50
63
Example Output 1
Your BMI is 28.0, you are slightly overweight.
since 63 ÷ (1.50 x 1.50) = 28

The testing code will check for print output that is formatted like one of the lines below:

"Your BMI is 18.28678, you are underweight."
"Your BMI is 22.0, you have a normal weight."
"Your BMI is 28.50752, you are slightly overweight."
"Your BMI is 32.56189, you are obese."
"Your BMI is 37.50000, you are clinically obese."
Example Input 2
1.60
96
Example Output 2
Your BMI is 37.49999999999999, you are clinically obese.
Example Input 3
1.71
73
Example Output 3
Your BMI is 24.96494647925858, you have a normal

## Leap year

Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February.

This is how you work out whether if a particular year is a leap year.

on every year that is divisible by 4 with no remainder

except every year that is evenly divisible by 100 with no remainder

unless the year is also divisible by 400 with no remainder

If english is not your first language or if the above logic is confusing, try using this flow chart .

Example Input 1
2400
Example Output 1
Leap year
Example Input 2
1989
Example Output 2
Not leap year

## Pizza order

Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

Small pizza (S): $15

Medium pizza (M): $20

Large pizza (L): $25

Add pepperoni for small pizza (Y or N): +$2

Add pepperoni for medium or large pizza (Y or N): +$3

Add extra cheese for any size pizza (Y or N): +$1

Example Input
L
Y
N
Example Output
Thank you for choosing Python Pizza Deliveries!
Your final bill is: $28.

## Love calculator

You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

- Take both people's names and check for the number of times the letters in the word TRUE occurs.

- Then check for the number of times the letters in the word LOVE occurs.

- Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be: "Your score is _x_, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be: "Your score is _y_, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is _z_."
e.g.

name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."
