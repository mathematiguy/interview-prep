# Implement an algorithm to determine if a string has all unique characters.


def is_unique(s):
    '''
    Returns True if s contains all unique characters
    '''

    char_counts = {}
    for ch in s:
        try:
            char_counts[ch]
            return False
        except KeyError:
            char_counts[ch] = 1

    return True


hints = ['#44', '#117', '#132']
for hint in hints:
    print(f"{hint}: {is_unique(hint)}")
