from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for char in plain_text:
    if char in alphabet:
        position = alphabet.index(char)
        new_position = position + shift_amount
        cipher_text += alphabet[new_position]
    else:
        cipher_text+=char
  print(f"Here's the encoded result: {cipher_text}")

def decrypt(plain_text, shift_amount):
  cipher_text = ""
  for char in plain_text:
    if char in alphabet:
        position = alphabet.index(char)
        new_position = position - shift_amount
        cipher_text += alphabet[new_position]
    else:
        cipher_text+=char
  print(f"Here's the decoded result: {cipher_text}")

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  shift= shift%26
  if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
  elif direction == "decode":
    decrypt(plain_text=text, shift_amount=shift)
  else:
    print("Please enter encode or decode.")

  result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if result == "no":
    should_continue = False
    print("Goodbye")