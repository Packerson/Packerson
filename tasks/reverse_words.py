def reverse_words(text):
    split_text = text.split(" ")
    array = []

    for word in split_text:
        array.append(word[::-1])

    array = " ".join(array)
    print(array)
    return array


reverse_words('double  spaced  words')


def reverse_words_2(text2):
    return ' '.join(w[::-1] for w in str.split(' '))
