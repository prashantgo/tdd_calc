def add(inputStr: str):
    """Add the numbers separated by a comma in a string"""
    if not isinstance(inputStr, str): return 0
    if inputStr == "": return 0
    return sum(map(lambda x: int(x), inputStr.split(",")))

def addNewLine(inputStr: str):
    """Add the numbers separated by a comma (new line included) in a string"""
    if not isinstance(inputStr, str): return 0
    if inputStr == "": return 0
    
    inputStr = inputStr.replace("\n", ",")
    return sum(map(lambda x: int(x), inputStr.split(",")))