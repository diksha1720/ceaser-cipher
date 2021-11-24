import util

def encrypt():
  text = input("Type your message to encode:\n").lower()
  shift = int(input("Type the shift number:\n"))
  encrypted_text=""
  for letter in text:
    new_ind=util.alphabet.index(letter)+shift
    if new_ind>25:
      new_ind=new_ind-26
    # print(new_ind)
    encrypted_text+=encrypted_text.join(util.alphabet[new_ind])
  print(f"The encrypted text is: {encrypted_text}")
  return encrypted_text


def decrypt():
  text = input("Type your message to decode:\n").lower()
  shift = int(input("Type the shift number:\n"))
  decrypted_text=""
  for letter in text:
    new_ind=util.alphabet.index(letter)-shift
    # print(new_ind)
    decrypted_text+=decrypted_text.join(util.alphabet[new_ind])
  print(f"The decrypted text is: {decrypted_text}")

a=5


choice="yes"
while choice=="yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  if direction=="encode":
    encrypt()
  elif direction=="decode":
    decrypt()
  else:
    print("Wrong option chosen!")
  choice=input("Type 'yes' if you want to decode otherwise choose 'no'\n")
  if choice!="yes":
    break
  



