import string

def ispangram(str1, alphabet=string.ascii_lowercase):

    alphaset = set(alphabet)

    str1 = str1.replace(' ', '')

    str1 = str1.lower()

    str1 = set(str1)

    return str1 == alphaset