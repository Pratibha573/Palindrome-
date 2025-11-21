import sys
if len(sys.argv) == 2:
    word = sys.argv[1]
    print("user input provided")
else:
    word = "madam"
    rev=word[::-1]
    if word == rev:
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")
