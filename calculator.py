def add(inputStr: str):
    if not isinstance(inputStr, str): return 0
    if inputStr == "": return 0
    return sum(map(lambda x: int(x), inputStr.split(",")))