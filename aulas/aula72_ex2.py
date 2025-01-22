
def impar_ou_par(num):
    if num % 2 == 0:
        return print('Número PAR')
    # else:
    return print('Número ÍMPAR')

impar_ou_par(6)
        
def impar_ou_par_melhorado(*num):
    for numero in num:
        if numero % 2 == 0:
            print(f'{numero = } PAR')
        else:
            print(f'{numero = } ÍMPAR')

impar_ou_par_melhorado(5,5,6,10,45)
impar_ou_par_melhorado(9876)