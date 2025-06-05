import random
import string

def generate_password(length=12, uppercase=True, lowercase=True, numbers=True, special_chars=True):
    characters = []
    
    if uppercase:
        characters.append(string.ascii_uppercase)
    if lowercase:
        characters.append(string.ascii_lowercase)
    if numbers:
        characters.append(string.digits)
    if special_chars:
        characters.append(string.punctuation)
    
    if not characters:
        raise ValueError("At least one character type must be selected")
    
    all_chars = ''.join(characters)
    password = []
    if uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if lowercase:
        password.append(random.choice(string.ascii_lowercase))
    if numbers:
        password.append(random.choice(string.digits))
    if special_chars:
        password.append(random.choice(string.punctuation))
    remaining_length = length - len(password)
    if remaining_length > 0:
        password.extend(random.choice(all_chars) for _ in range(remaining_length))
    
    random.shuffle(password)
    
    return ''.join(password)

def get_user_input():
    print("Password Generator Settings:")
    
    try:
        length = int(input("Enter password length (8-64): "))
        if not 8 <= length <= 64:
            print("Length must be between 8 and 64. Using default 12.")
            length = 12
    except ValueError:
        print("Invalid input. Using default length 12.")
        length = 12
    
    uppercase = input("Include uppercase letters? (Y/n): ").lower() != 'n'
    lowercase = input("Include lowercase letters? (Y/n): ").lower() != 'n'
    numbers = input("Include numbers? (Y/n): ").lower() != 'n'
    special_chars = input("Include special characters? (Y/n): ").lower() != 'n'
    
    return length, uppercase, lowercase, numbers, special_chars

def main():
    print("=== Password Generator ===")
    
    while True:
        length, uppercase, lowercase, numbers, special_chars = get_user_input()
        
        try:
            password = generate_password(length, uppercase, lowercase, numbers, special_chars)
            print("\nGenerated Password:", password)
        except ValueError as e:
            print(f"Error: {e}")
        
        again = input("\nGenerate another password? (Y/n): ").lower()
        if again == 'n':
            break
    
    print("\nThank you for using the Password Generator!")

if __name__ == "__main__":
    main()
