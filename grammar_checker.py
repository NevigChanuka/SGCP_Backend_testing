import pandas as pd


def letters_to_unicode(letters):
    return ' '.join(f"U+{ord(char):04X}" for char in letters)

word =  "ගය"


verb_list = []



























# def unicode_to_letters(unicode_string):
#     try:
#         # Split the input by spaces and convert each to a character
#         letters = ''.join(chr(int(code, 16)) for code in unicode_string.split())
#         return letters
#     except ValueError:
#         return "Invalid Unicode input!"
#
# if __name__ == "__main__":
#     user_input = input("Enter Unicode codes (e.g., U+0DC0 U+0DBA U+0DD2): ").replace("U+", "").strip()
#     result = unicode_to_letters(user_input)
#     print("Converted Letters:", result)


# def unicode_to_letters(unicode_string):
#     try:
#         # Split the input by spaces and convert each to a character
#         letters = ''.join(chr(int(code, 16)) for code in unicode_string.split())
#         return letters
#     except ValueError:
#         return "Invalid Unicode input!"
#

#
# if __name__ == "__main__":
#     choice = input("Choose an option: (1) Unicode to Letters (2) Letters to Unicode: ")
#     if choice == "1":
#         user_input = input("Enter Unicode codes (e.g., U+0DC0 U+0DBA U+0DD2): ").replace("U+", "").strip()
#         result = unicode_to_letters(user_input)
#         print("Converted Letters:", result)
#     elif choice == "2":
#         user_input = input("Enter letters: ")
#         result = letters_to_unicode(user_input)
#         print("Unicode Codes:", result)
#     else:
#         print("Invalid choice!")

