import re
import random

# Optional: List of commonly weak passwords
common_passwords = ["password", "123456", "qwerty", "letmein", "password123", "admin"]

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Check if in common list
    if password.lower() in common_passwords:
        print("❌ This password is too common. Choose something more secure.")
        return

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("• Make it at least 8 characters long.")

    # Uppercase & lowercase check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("• Include both uppercase and lowercase letters.")

    # Digit check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("• Add at least one digit (0-9).")

    # Special character check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("• Use a special character (!@#$%^&*).")

    # Print final score
    print(f"\n🔍 Password Score: {score}/4")

    # Strength level
    if score == 4:
        print("✅ Strong Password!")
    elif score == 3:
        print("⚠️ Moderate Password – You can make it stronger.")
    else:
        print("❌ Weak Password – Improve using the suggestions below:")
        for tip in feedback:
            print(tip)

# Optional: Password generator
def generate_strong_password(length=12):
    if length < 8:
        length = 8
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    password = ''.join(random.sample(chars, length))
    return password

# Main program
def main():
    print("🔐 Password Strength Checker\n")
    password = input("Enter your password: ").strip()
    check_password_strength(password)

    # Suggestion
    suggest = input("\nWould you like a strong password suggestion? (yes/no): ").lower()
    if suggest in ['yes', 'y']:
        new_password = generate_strong_password()
        print(f"💡 Suggested Strong Password: {new_password}")

# Run
if __name__ == "__main__":
    main()
