#Encryption Program
import random
import string
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

#ENCRYPTION
plain_text = input("Enter the text to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
print(f"Original Text: {plain_text}")
print(f"Encrypted Text: {cipher_text}")

#DECRYPTION
cipher_text = input("Enter the text to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]
print(f"Decrypted Text: {plain_text}")
print(f"Encrypted Text: {cipher_text}")