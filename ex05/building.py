import sys


def countTypeLetters():
    """
    Cette fonction prend une chaîne en argument et affiche le nombre
    de lettres majuscules, minuscules, signes de ponctuation, espaces
    et chiffres dans cette chaîne.
    """
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        sys.exit(1)
    elif len(sys.argv) == 1:
        input_str = input("What is the text to count?\n")
    else:
        input_str = sys.argv[1]

    upperLetter = 0
    lowerLetter = 0
    punctuationMarks = 0
    spaces = 0
    digits = 0
    punctuation = ".,:;!?-'\"()[]{}<>/\\|_*&^%$#@`~+=()"

    for i in input_str:
        if i.isupper():
            upperLetter += 1
        elif i.islower():
            lowerLetter += 1
        elif i.isspace():
            spaces += 1
        elif i.isdigit():
            digits += 1
        elif i in punctuation:
            punctuationMarks += 1

    print(f"The text contains {len(input_str)} characters:")
    print(f"{upperLetter} upper letters")
    print(f"{lowerLetter} lower letters")
    print(f"{punctuationMarks} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    countTypeLetters()


if __name__ == "__main__":
    main()
