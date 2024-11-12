from sys import argv


def main():
    # check if the num of args is corret (2)
    assert len(argv) == 2, "the arguments are bad"

    text = argv[1]
    # check if every char of the string is alphnum or space
    for c in text:
        if c.isalnum() or c.isspace():
            continue
        else:
            raise AssertionError("the arguments are bad")
    print(text)
    # Build a new string with characters converted to uppercase if needed
    new_text = ''.join([to_upper_if_needed(char) for char in text])
    print(new_text)
    res = str_convert_to_morse(new_text)
    print(res)
    return 0


def to_upper_if_needed(c):
    if not c.isupper():  # Check if the character is not in uppercase
        return c.upper()  # Convert to uppercase if needed
    return c


def str_convert_to_morse(str):
    morse_dico = {
        'A': '.-', 'B': '-...',
        'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-',
        'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--',
        'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', ' ': '/ '}

    str_converted = ''
    for c in str:
        str_converted += morse_dico[c] + ' '
        # Concatenate Morse code with a space
    return str_converted.strip()  # Remove any trailing space


if __name__ == "__main__":
    main()
