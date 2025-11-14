def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def main():
    user_input = input("Enter a string: ")

    # Check length
    if len(user_input) < 4:
        print("Error: Input must contain at least 4 characters.")
        return

    # Palindrome check
    if is_palindrome(user_input):
        print("True – It is a palindrome.")
    else:
        print("False – Not a palindrome.")

if __name__ == "__main__":
    main()
