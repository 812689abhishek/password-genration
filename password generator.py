import random
import string

def generate_password(length, include_special_chars=True):
    # Define the character sets
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation if include_special_chars else ''
    
    # Create the character pool
    char_pool = letters + digits + special_chars
    
    # Generate the password
    if length <= 0:
        return "Password length must be greater than 0"
    
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def get_user_input():
    try:
        length = int(input("Enter the desired length of the password: "))
        include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
        return length, include_special_chars
    except ValueError:
        print("Invalid input. Please enter a numeric value for the length.")
        return None, None

def main():
    length, include_special_chars = get_user_input()
    if length is not None:
        password = generate_password(length, include_special_chars)
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
