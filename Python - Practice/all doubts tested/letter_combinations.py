def letterCombinations(digits: str):
    if len(digits) == 0:
        return []
    alp = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }
    length = [len(alp[c]) for c in digits]
    print(length)


letterCombinations("237")
