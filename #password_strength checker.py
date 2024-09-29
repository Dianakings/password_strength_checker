#password_strength checker
import re

def check_password_strength(password):
    # Initialize score
    score = 0
    suggestions = []

    # Check if the password has at least 8 characters
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Password is too short! Must be at least 8 characters.")

    # Check for both uppercase and lowercase letters
    if re.search("[a-z]", password):
        score += 1
    else:
        suggestions.append("Password must contain at least one lowercase letter.")

    if re.search("[A-Z]", password):
        score += 1
    else:
        suggestions.append("Password must contain at least one uppercase letter.")

    # Check for digits
    if re.search("[0-9]", password):
        score += 1
    else:
        suggestions.append("Password must contain at least one digit.")

    # Check for special characters
    if re.search("[@#$%^&+=!]", password):
        score += 1
    else:
        suggestions.append("Password must contain at least one special character (@, #, $, etc.).")

    # Provide feedback based on the score
    if score == 5:
        return "Password is strong!"
    elif score >= 3:
        return f"Password is moderate. To improve: {', '.join(suggestions)}"
    else:
        return f"Password is weak. To improve: {', '.join(suggestions)}"

def automate_password_check(passwords):
    for password in passwords:
        print(f"Checking password: {password}")
        result = check_password_strength(password)
        print(result)
        print("-" * 50)

# List of passwords to check automatically
passwords = [
    "Pass123!",
    "weakpass",
    "StrongPa$$word123",
    "password123",
    "12345"
    "LatifaH.123@1",
]

# Automate password checking
automate_password_check(passwords)
