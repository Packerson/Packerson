import re
def pig_it(text):
    array = text.split()
    new_array = []
    s = '[@_!#$%^&*()<>?/\|},.{~:]'
    for element in array:
        if not re.findall(('^[\d|\.|\,!?]+'), element):
            element = element[1::] + element[0] + "ay"
            new_array.append(element)
        else:
            new_array.append(element)
    return (" ").join(new_array)

pig_it('Hello world ! .')     # elloHay orldway !