import random

def generate_random_number():
    return random.randint(1000, 9999)

# Generate a random 4-digit number
random_number = generate_random_number()
print("Random 4-digit number:", random_number)
