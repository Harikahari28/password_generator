import random
import string

def generate_password(length=12):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    num_passwords = int(input("How many passwords would you like to generate? "))
    length = int(input("Enter the length of each password: "))

    print("\nGenerating passwords...\n")

    passwords = [generate_password(length) for _ in range(num_passwords)]

    for i, password in enumerate(passwords, start=1):
        print(f"Password {i}: {password}")

if __name__ == "__main__":
    main()
