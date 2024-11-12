# from curses.ascii import isdigit, islower, isupper
from sys import argv
import sys


def main():
    char_num = 0
    upp_num = 0
    low_num = 0
    punc_num = 0
    spa_num = 0
    dig_num = 0

    assert len(argv) <= 2, "Too much args"
    if len(argv) < 2:
        print("What is the text to count?")
        text = sys.stdin.readline()
    elif len(argv) == 2:
        text = argv[1]
    if isinstance(text, str):
        for i in text:
            char_num += 1
            if text[char_num - 1].isupper():
                upp_num += 1
            if text[char_num - 1].islower():
                low_num += 1
            if text[char_num - 1].isspace():
                spa_num += 1
            if text[char_num - 1].isdigit():
                dig_num += 1
            if ispunct(text[char_num - 1]):
                punc_num += 1
        print(f"The text contains {char_num} characters:")
        print(f"{upp_num} upper letters")
        print(f"{low_num} lower letters")
        print(f"{punc_num} punctuation marks")
        print(f"{spa_num} spaces")
        print(f"{dig_num} digits")
    return 0


# def main():
#     char_num = 0
#     upp_num = 0
#     low_num = 0
#     punc_num = 0
#     spa_num = 0
#     dig_num = 0

#     if len(argv) < 2:
#         text = input("What is the text to count?\n")
#     elif len(argv) == 2:
#         text = argv[1]
#     else:
#         text = 0
#         print("Assertion Error: Too much args")
#     print(text, end="")
#     text = text.replace('\\', ' ').replace('\n', ' ').replace('\r', ' ')
#     print(text)
#     if isinstance(text, str):
#         for i in text:
#             char_num += 1
#             if text[char_num - 1].isupper():
#                 upp_num += 1
#             if text[char_num - 1].islower():
#                 low_num += 1
#             if text[char_num - 1].isspace():
#                 spa_num += 1
#             if text[char_num - 1].isdigit():
#                 dig_num += 1
#             if ispunct(text[char_num - 1]):
#                 punc_num += 1
#         # print(f"'{char}' is a punctuation mark.")
#         print(f"The text contains {char_num} characters:")
#         print(f"{upp_num} upper letters")
#         print(f"{low_num} lower letters")
#         print(f"{punc_num} punctuation marks")
#         print(f"{spa_num} spaces")
#         print(f"{dig_num} digits")
#     return 0


def ispunct(c):
    """
    ispunct check if the caracter c is in the list punctuation_marks
    and return c if true
    """
    punctuation_marks = '''!"#$%&'()*+,-./:;<=>?@[]\\^_`{|}~'''
    return c in punctuation_marks

    # if isdigit(text[char_num -1]):
    #     dig_num += 1


if __name__ == "__main__":
    main()
