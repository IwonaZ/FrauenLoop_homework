import re

def valid(str):
    if re.match("\d{4}$|\d{6}$", str):
        return True
    else:
        return False