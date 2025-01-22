"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
letras_acertadas = ''
palavra_secreta = "combustivel".upper()
palavra_formatada = ''
qts_tentativas = 0

while True:
    letra_user = input("Digite uma letra que vc acha que está na palavra secreta: ")
    letra_user = letra_user.upper()
    
    if len(letra_user) > 1:
        print("Digite apenas uma letra.")
        continue

    if letra_user in palavra_secreta:
        palavra_formatada = ''
        if letra_user not in letras_acertadas:
            letras_acertadas = letras_acertadas + letra_user   

        for letra in palavra_secreta:
            imprimir = True

            for letra_acerta in letras_acertadas:

                if letra == letra_acerta:
                    #print(letra.upper(), end="")
                    palavra_formatada += letra.upper()
                    imprimir = False
                    
            if imprimir == True:
                #print("*",end="")
                palavra_formatada += "*"
        print(f"Letras acertadas: {palavra_formatada}")
    else:
        if len(palavra_formatada) == 0:
            palavra_formatada = "*" * len(palavra_secreta)
            print(f"Letras acertadas: {palavra_formatada}")
        else:
            print(f"Letras acertadas: {palavra_formatada}")

    palavra_user = input("Qual vc acha que é a palavra secreta? ").upper()

    qts_tentativas += 1
    
    if palavra_user == palavra_secreta:
        print(f"Acertou a palavra secreta é {palavra_secreta}")
        print(f"Foram necessárias {qts_tentativas} tentativas para acertar")
        break
    else:
        print(f"{palavra_user} não é a palavra secreta")
