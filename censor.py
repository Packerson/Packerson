def censor(c):
    s = c.split(" ")
    new = []
    for word in s:
        if word == "Java" or word == "PHP" or word == "C#" or word == "Ruby":
            word = "****"
            new.append(word)
        else:
            new.append(word)
    new_2 = " ".join(new)
    return new_2

#można jeszcze przemnożyć ilość znaków razy gwiazdka


show = censor("łancuch tekstów C# PHP php")
print(show)


def censor_2(text):
    forbidden = ["Java", "PHP", "C#", "Ruby"]
    s = text.split(" ")
    new = []
    for word in s:
        if word in forbidden:
            word = "****"
            new.append(word)
        else:
            new.append(word)
    new_2 = " ".join(new)
    return new_2

a = censor_2("Java is the best, but PHP is the bestest!")
print(a)


def censor_3(words):
    censored = ("Java", "PHP", "Ruby", "C#")
    sentence = ""
    splitlist = []
    words = words.split()

    for word in words:
        if word in censored:
            cen = len(word) * "*"
            sentence += cen + " "
        else:
            sentence += word + " "
    return sentence


zdanie = "Java, is better than PHP"
print(censor_3(zdanie))

