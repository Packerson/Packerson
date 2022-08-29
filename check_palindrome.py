def check_palindrome(x):
    print(x)
    letters = list(x)
    odwrocona = letters[::-1]
    if letters == odwrocona:
        result = True
    else:
        result = False

    return result


a = check_palindrome("1 ABCCBA 1")
print(a)

def check_palindrome2(sentence):
    sentence = sentence.lower()
    sentence = [w for w in sentence if w.isalnum()]
    return sentence == sentence[::-1]


y = check_palindrome2("1Kajak, kajak,kajak1.")
print(y)

