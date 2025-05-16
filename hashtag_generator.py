def generate_hashtag(s):
    if len(s) == 0:
        return False
    words = s.split(" ")
    result = '#'
    total_chars = 1
    for word in words:
        result += word.capitalize()
        total_chars += len(word)
    if total_chars > 140:
        return False
    else:
        return result

def main():
    s = "hello world"

    print(generate_hashtag(s))


if __name__ == "__main__":
    main()
