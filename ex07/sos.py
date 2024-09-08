import sys


def encodeToMorse(text):
    """
    This function takes a text, and encodes it to morse code.
    input: text
    output: prints the morse code
    """
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
    }

    try:
        morse_code = []
        for i in text:
            morse_code.append(NESTED_MORSE[i])

        print(" ".join(morse_code))

    except Exception:
        print("AssertionError: the arguments are bad")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        sys.exit(1)

    try:
        encodeToMorse(str(sys.argv[1].upper()))
    except Exception:
        print("AssertionError: the arguments are bad")
        sys.exit(1)


if __name__ == "__main__":
    main()
