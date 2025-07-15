# Codewars Challenge
# link: https://www.codewars.com/kata/57e0206335e198f82b00001d/train/python

def esrever(st):
    # Separate punctuation at the end
    if st and st[-1] in ('!', '?', '.'):
        punct = st[-1]
        st = st[:-1]
    else:
        punct = ''
    # Reverse words and letters in words
    words = st.split()
    reversed_words = [word[::-1] for word in words[::-1]]
    result = ' '.join(reversed_words) + punct
    return result
print(esrever("Hello World!"))  # Output: !dlroW olleH