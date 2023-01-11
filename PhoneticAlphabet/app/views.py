from django.shortcuts import render

# Create your views here.
def app(request):
    if request.method == 'POST':
        phonetic_alphabet = {
            'a': 'alpha', 'b': 'bravo', 'c': 'charlie', 'd': 'delta',
            'e': 'echo', 'f': 'foxtrot', 'g': 'golf', 'h': 'hotel',
            'i': 'india', 'j': 'juliet', 'k': 'kilo', 'l': 'lima',
            'm': 'mike', 'n': 'november', 'o': 'oscar', 'p': 'papa',
            'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
            'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray',
            'y': 'yankee', 'z': 'zulu', '@': 'at', '.': 'dot'
        }
        frase = request.POST['frase']
        frase = frase.lower()
        
        f = []
        
        for i in frase:
            if i in phonetic_alphabet:
                f.append(f'{i.upper()} -> {phonetic_alphabet[i].capitalize()}')
            else:
                f.append(i)
        
        return render(request, 'app/app.html', context={'phonetic':f, 'frase':frase})

    return render(request, 'app/app.html')
