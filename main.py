alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)
end = False
while not end:
   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
   def encrypt(plain_text, shift_amount):
      c = ""
      for char in plain_text:
         if char in alphabet:
            a = alphabet.index(char)
            b = alphabet[a + shift_amount]
            c += b
      print(c)

   def decrypt(plain_text, shift_amount):
      f = ""
      for char in plain_text:
         if char in alphabet:
            d = alphabet.index(char)
            e = alphabet[d - shift_amount]
            f += e
      print(f)
   plain_text = input("Type your message:\n").lower()
   shift_amount = int(input("Type the shift number:\n"))
   if shift_amount>26:
      shift_amount=shift_amount%26
   if direction == "encode":
      encrypt(plain_text, shift_amount)
   elif direction == "decode":
      decrypt(plain_text, shift_amount)
   h=input("type yes to go again or no to stop")
   if h=="no":
      end = True
      print("thank you for using caeser cipher!")



