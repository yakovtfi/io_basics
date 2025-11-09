
def atbash_cipher(text):
    result=""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result+=chr(155 - ord(char))
            else:

                result+=chr(219 - ord(char))
        else:
            result+=char
    return result

message=input("Enter the message: ")
encoded = atbash_cipher(message)
with open("encrypted.txt","w") as file:
    file.write(encoded)
print("Encrypted message saved to encrypted.txt")

with open("encrypted.txt", "r") as file:
    encrypted_text = file.read()

decoded = atbash_cipher(encrypted_text)
print("Decrypted message:", decoded)

