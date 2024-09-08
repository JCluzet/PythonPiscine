import sys
from ft_filter import ft_filter


def main():
    """
    It takes arguments from the command line: a string and an integer.
    It filters and returns a list of words with
    a length greater than the given integer.
    """
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        sys.exit(1)

    try:
        string_arg = sys.argv[1]
        number_arg = int(sys.argv[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        sys.exit(1)

    words = string_arg.split()
    for word in words:
        if not word.isalnum():
            print("AssertionError: the arguments are bad")
            sys.exit(1)

    filtered_words = ft_filter(lambda word: len(word) > number_arg, words)
    print(list(filtered_words))


if __name__ == "__main__":
    main()
