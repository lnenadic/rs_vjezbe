vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."


def count_vowels_and_consonants(text):
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1

    return {'vowels': vowel_count, 'consonants': consonant_count}


print(count_vowels_and_consonants(tekst))
