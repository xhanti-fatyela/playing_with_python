def greet(lang):
    if lang == 'es':
        return 'Hola ' + name
    elif lang == 'fr':
        return 'Bonjour' + name
    else:
        return 'Hello'


name = input('Enter Your Name')

print(greet('es'))
