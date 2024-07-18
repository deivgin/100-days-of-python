import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text: str, shift: int, direction: str):
  encode = direction == 'encode'
  decryption: list[str] = []

  for letter in text:
    if letter not in alphabet:
      decryption.append(letter)
      continue

    text_index = alphabet.index(letter)
    shift_index = (text_index + shift) % 26 if encode else (text_index - shift) % 26
    decryption.append(alphabet[shift_index])

  print(f"The {'encoded' if encode else 'decode'} text is {''.join(decryption)}")

def init():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

  if direction != 'encode' and direction != 'decode':
    print("Invalid input.")
    exit(1)

  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  if(shift > 26):
    shift %= 26

  return text, shift, direction

def start():
  text, shift, direction = init()
  caesar(text, shift, direction)

start()
