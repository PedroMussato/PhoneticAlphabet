phonetic_alphabet = {
    'a': 'alpha', 'b': 'bravo', 'c': 'charlie', 'd': 'delta',
    'e': 'echo', 'f': 'foxtrot', 'g': 'golf', 'h': 'hotel',
    'i': 'india', 'j': 'juliet', 'k': 'kilo', 'l': 'lima',
    'm': 'mike', 'n': 'november', 'o': 'oscar', 'p': 'papa',
    'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray',
    'y': 'yankee', 'z': 'zulu', '@': 'at', '.': 'dot', '0':'zero'
    '1':'one','2':'two','3':'three','4':'four','5':'five','6':'six',
    '7':'seven','8':'eight','9':'nine',
}

while True:
    frase = input('Type the frase: ')
    frase = frase.lower()

    print('\n')

    for i in frase:
        if i in phonetic_alphabet:
            print(phonetic_alphabet[i].capitalize())
        else:
            print(i)
