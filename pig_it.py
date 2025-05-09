def pig_it(text):
    words = text.split(" ")
    pig_words = [] 
    punctuation = "!.?"
    
    for word in words:
        if word not in punctuation:
            first_letter, word = word[0], word[1:]
            word = word + first_letter + "ay"
        pig_words.append(word)
    text = " ".join(pig_words)
    return text


def main():
    print(pig_it('Pig latin is cool'))
    print(pig_it('This is my string'))
    print(pig_it('Hello world !'))

if __name__ == "__main__":
    main()
