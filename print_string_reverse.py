str = "A long string to test this algorithm"

def easyversion(s):
    # You have a string:
    # Split the string (at word boundary -- no arguments to split):

    splitted = str.split()
    print(splitted)
    # Reverse the array obtained -- either using ranges or a function

    reversed = splitted[::-1]
    print(reversed)
    # Concatenate all words with spaces in between -- also known as joining.

    result = " ".join(reversed)
    print(result)


def hardversion(s):

    spaces = ' '
    while i < len(s):
        if s[i] not in spaces:
            print(i)
