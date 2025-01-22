frase = 'O Python é uma linguagem de programação '\
        'multiparadiga. '\
        'Python foi criado por Guido van Rossum.'
frase = frase.split()
frase = ''.join(frase).lower()
#print(frase)

num_letra_mais_repetida = 0
letra_mais_repetida = ''
#letras_que_ja_foram = ''
i = 0
while i < len(frase):
    letra = frase[i]

    # if letra in letras_que_ja_foram:
    if letra == ' ':
        i += 1
        continue
    #letras_que_ja_foram = letras_que_ja_foram + letra
    if frase.count(letra) > num_letra_mais_repetida:
        num_letra_mais_repetida = frase.count(letra)
        letra_mais_repetida = letra
 
    #print(letra, frase.count(letra))
    i += 1
else:
    print(f'A letra mais repetida foi "{letra_mais_repetida}" com '\
        f'{num_letra_mais_repetida} aparições.')
    

