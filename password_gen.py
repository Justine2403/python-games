import random
import string

def password():
    num_pass = int(input("How many password ? "))
    num_char = int(input("How many characters ? "))
    
    # Combining letter (lowercase and uppercase) + number + punctuation symbols in one list of possible characters
    characters = string.ascii_letters + string.digits + string.punctuation

    for i in range(num_pass):
        print(''.join(random.choice(characters) for j in range(num_char)))

password()