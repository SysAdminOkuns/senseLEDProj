lowcase_alphabet = "abcdefghijklmnopqrstuvwxyz"
uppercase_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
flip_uppercase = uppercase_alphabet[::-1]


def encrypt_message(msg, kval):
    newMessage = ""
    for char in msg:
        if char in lowcase_alphabet:
            position = lowcase_alphabet.find(char)
            newPosition = (int(position) + int(kval)) % 26
            newMessage += lowcase_alphabet[newPosition]
        elif char in flip_uppercase:
            position = flip_uppercase.find(char)
            newPosition = (int(position) + int(kval)) % 26
            newMessage += flip_uppercase[newPosition]
        elif char == " ":
            newMessage += "@"
        else:
            newMessage += "%^"
    return newMessage


def decrypt_message(c_msg, kval):
    deci_msg = ""
    for char in c_msg:
        if char in lowcase_alphabet:
            reversed_pos = lowcase_alphabet.find(char)
            nposition = (int(reversed_pos) - int(kval)) % 26
            deci_msg+= lowcase_alphabet[nposition]
        elif char in flip_uppercase:
            reversed_pos = flip_uppercase.find(char)
            nposition = (int(reversed_pos) - int(kval)) % 26
            deci_msg += flip_uppercase[nposition]
        elif char in "@":
            deci_msg += " "
        elif char == "%":
            deci_msg += "!"
    return deci_msg




message = input("Enter a message to encrypt: ")
key = input("Enter your secret key between 0-25: ")

safe_msg = encrypt_message(message, key)
print(safe_msg)

decipher_msg = decrypt_message(safe_msg, key)
print(decipher_msg)

#print(flip_uppercase.find("Z"))

