# Tasks for day 4

## Heads or Tails

You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

e.g. 1 means Heads 0 means Tails

## Banker roulette

You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

Assume that names works like this:

input area: x, y, z,
names = ["x", "y", "z"]
Example Input
Angela, Ben, Jenny, Michael, Chloe
Note: notice that there is a space between the comma and the next name.

Example Output
Michael is going to buy the meal today!

## Treasure map

You are going to write a program that will mark a spot on a map with an X.

Your job is to write a program that allows you to mark a square on the map using a letter-number system.

So an input of A3 should place an X at the position shown below:

- First, your program must take the user input and convert it to a usable format.

- Next, you need to use that input to update your nested list with an "X". Remember that your nested list map actually looks like this:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
Example Input 1
B3
Example Output 1
Hiding your treasure! X marks the spot.
['⬜️', '️⬜️', '️⬜️']
['⬜️', '⬜️', '️⬜️']
['⬜️️', 'X', '⬜️️']
Example Input 2
B1
Example Output 2
Hiding your treasure! X marks the spot.
['⬜️', 'X', '️⬜️']
['⬜️', '⬜️', '️⬜️']
['⬜️️', '⬜️️', '⬜️️']
