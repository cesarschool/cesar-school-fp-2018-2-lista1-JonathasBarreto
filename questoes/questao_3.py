## QUESTÃO 3 ##
# Escreva um programa que calcule a área de um círculo, o diâmetro e o comprimento 
# da circunferência. Solicite que o usuário insira o raio e imprima uma mensagem 
# agradável de volta para o usuário com a resposta. 
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
from math import *

def main():
    raio = float(input("Informe o raio: "))
    area = pi * pow(raio,2)
    diam = raio * 2
    comp = 2 * pi * raio
    print("com o raio ", raio, " obtemos a área de ",area,", diâmetro de ",diam,", e comprimento de ",comp)

    
if __name__ == '__main__':
    main()
