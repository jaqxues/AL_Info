vowels = "aeiou"
vowels += vowels.upper()


def no_vowels(str1):
    for vowel in vowels:
        if vowel in str1:
            return False
    else:
        return True
