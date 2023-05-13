import re 


def check_format(string):
    pattern = r"^\w+\s*-\s*\w+$"
    match = re.match(pattern, string)
    if match:
        return True
    else:
        return False
    
def convert_format(string):
    pattern = r"\s*-\s*"
    converted_string = re.sub(pattern, " ", string)
    return converted_string