import string
import secrets


def analyze_password(password):
    score = 0
    suggestions = []

    # Length checks
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1

    # Character-type checks
    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter (A-Z).")

    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter (a-z).")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one number (0-9).")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        suggestions.append("Add at least one special character (such as !, @, or #).")

    # A simple warning; repeated characters do not change the score.
    if len(password) != len(set(password)):
        suggestions.append("Avoid using the same character repeatedly.")

    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return strength, score, suggestions


def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(characters) for _ in range(length))


def main():
    print("=" * 45)
    print("          PASSWORD STRENGTH ANALYZER")
    print("=" * 45)
    print("Use a fictional password for testing.\n")

    password = input("Enter a password to analyze: ")

    if not password:
        print("\nNo password entered. Please run the program again.")
        return

    strength, score, suggestions = analyze_password(password)

    print("\n--- Analysis Result ---")
    print("Strength:", strength)
    print("Basic score:", str(score) + "/6")

    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("\nYour password meets all the basic checks.")

    print("\nExample randomly generated password:")
    print(generate_password())
    print("\nAnalysis completed.")


if __name__ == "__main__":
    main()
