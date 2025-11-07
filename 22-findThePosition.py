def position(letter):
    """
    Given a letter, returns its 1-based position in the alphabet.
    Example: position('a') -> "Position of alphabet: 1"
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return f"Position of alphabet: {alphabet.find(letter) + 1}"

print(position("a"))