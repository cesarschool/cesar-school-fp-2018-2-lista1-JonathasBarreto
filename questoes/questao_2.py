## QUESTÃO 2 ##
# Escreva um programa que converta uma temperatura digitada em °C (graus celsius) 
# para °F (graus fahrenheit). 
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    C = int(input("Informe a temperatura em celcius que deseja converter para fahrenheit: "))
    F = ((9*C)/5)+32
    print("o valor em fahrenheit é de: ",F, "F")



if __name__ == '__main__':
    main()
