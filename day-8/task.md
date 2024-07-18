# Tasks for day 8

## Paint area calculator

You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height x wall width) ÷ coverage per can.

e.g. Height = 2, Width = 4, Coverage = 5

number of cans = (2 \* 4) / 5 = 1.6
But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

Example Input
3
9
Example Output
You'll need 6 cans of paint.

## Prime numbers

Prime numbers are numbers that can only be cleanly divided by themselves and 1.

You need to write a function that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.

Example Input 1
73
Example Output 1
It's a prime number.
Example Input 2
75
Example Output 2
It's not a prime number.

## Caesar cipher

### Part 1

- Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

- Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.

e.g.
plain_text = "hello"
shift = 5
cipher_text = "mjqqt"
print output: "The encoded text is mjqqt"

- Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

### Part 2

- Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

- Inside the 'decrypt' function, shift each letter of the 'text' _backwards_ in the alphabet by the shift amount and print the decrypted text.
  #e.g.
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"

- Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt _AND_ decrypt a message.

### Part 3

- Combine the encrypt() and decrypt() functions into a single function called caesar().

- Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

### Part 4

- Import and print the logo from art.py when the program starts.

- What if the user enters a shift that is greater than the number of letters in the alphabet?

  - running the program and entering a shift number of 45.
  - Add some code so that the program continues to work even if the user enters a shift number greater than 26.

- What happens if the user enters a number/symbol/space?

  - Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
  - e.g. start_text = "meet me at 3"
  - end_text = "•••• •• •• 3"
