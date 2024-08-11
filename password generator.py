import random
import string

def generate_password(length=12, use_special_chars=True):
    # Define the characters to use in the password
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation if use_special_chars else ''

    # Combine all characters
    all_characters = letters + digits + special_chars

    # Ensure the password length is at least 1
    if length < 1:
        raise ValueError("Password length must be at least 1")

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 1:
            raise ValueError("Password length must be at least 1")
        
        use_special_chars_input = input("Include special characters? (yes/no): ").strip().lower()
        use_special_chars = use_special_chars_input in ['yes', 'y']

        # Generate and display the password
        password = generate_password(length, use_special_chars)
        print(f"Generated password: {password}")

    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
