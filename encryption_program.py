#Encryption Program
import random
import string
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

print(f"chars: {chars}")
print(f"key: {key}")

#ENCRYPTION
plain_text = input("Enter the text to encrypt: ")
cipher_text = ""

