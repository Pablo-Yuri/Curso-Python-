texto = "Python é uma linguagem de programação"
# print(texto.split())

remover_palavras = "uma de programação "

def remover(texto, palavras_a_remover):
    palavras_texto = texto.lower().split()
    p_remover = palavras_a_remover.lower().split()
    frase_final = ""
    for palavra in palavras_texto:
            # print(palavra,p_remover)
            if palavra not in p_remover:
                frase_final += f"{palavra} "
    return frase_final.strip()

texto_final = remover(texto, remover_palavras)
print(f"texto inicial: {texto}\nRemover palavras: {remover_palavras}\nTexto final: {texto_final}")

