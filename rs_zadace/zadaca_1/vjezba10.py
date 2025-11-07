tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."


def brojanje_riječi(tekst):
    words = tekst.split()
    count = {}

    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    return count


print(brojanje_riječi(tekst))
