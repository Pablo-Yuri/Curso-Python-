# Exemplo de uso dos sets
letras = set()
while True:
    letra = input('Digite: ')
    
    if not letra.isdigit() and len(letra) <= 1:
        letras.add(letra.lower())

    if 'l' in letras:
        print('PARABÉNS')
        break

    print(letras)