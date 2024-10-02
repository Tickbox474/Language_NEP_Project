import random
import string

def generate_random_pass(length=15):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    password = ''.join(random.choice(characters) for i in range (length))
    return password

new_number = generate_random_pass()
print(f"Your new password would be: \033[4m{new_number}\033[0m")
print("Please keep this safe somewhere")
