def add(inputStr: str):
    """Add the numbers separated by a comma in a string"""
    if not isinstance(inputStr, str): return 0
    if inputStr == "": return 0
    return sum(map(lambda x: int(x), inputStr.split(",")))

def addNewLine(inputStr: str):
    """Add the numbers separated by a comma (new line included) in a string"""
    if not isinstance(inputStr, str): return 0
    if inputStr == "": return 0

    inputNumbers = inputStr.replace("\n", ",").split(",")
    return sum(map(lambda x: int(x), inputNumbers))

def addAllowDelimiters(inputStr: str):
    """Add the numbers separated by a delimiter in a string"""
    if not isinstance(inputStr, str): return 0
    if inputStr == "" or len(inputStr) <= 4: return 0

    delimiter = inputStr[2]
    inputNumbers = inputStr[4:].split(delimiter)
    return sum([int(number) for number in inputNumbers if number.isdigit()])

def addDisallowNegative(inputStr: str):
    """Add the numbers separated by a delimiter in a string"""
    if not isinstance(inputStr, str): return 0
    if inputStr == "" or len(inputStr) <= 4: return 0

    delimiter = inputStr[2]
    inputNumbers = inputStr[4:].split(delimiter)
    positiveNumbers = [int(number) for number in inputNumbers if number.lstrip("-").isdigit()]
    negativeNumbers = [number for number in inputNumbers if number.lstrip("-").isdigit() and int(number) < 0]

    if negativeNumbers:
        negativeNumbers = ",".join(negativeNumbers)
        raise Exception(f"negative numbers not allowed {negativeNumbers}")

    return sum(positiveNumbers)