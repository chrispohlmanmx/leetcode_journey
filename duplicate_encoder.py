def duplicate_encode(word):
    chars = {}
    for char in word:
        char = char.lower()
        if char not in chars:
            chars[char.lower()] = 1
        else:
            chars[char] += 1
    
    encoded_string = ""
    for char in word:
        char = char.lower()
        if chars[char] == 1:

            encoded_string += '('
        else:
            encoded_string += ')'
    return encoded_string

def main():
    print(duplicate_encode("din"))
    print(duplicate_encode("recede"))
    print(duplicate_encode("Success"))
    print(duplicate_encode("(( @"))

if __name__ == "__main__":
    main()
