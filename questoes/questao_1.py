## QUESTÃO 1 ## 
# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o 
# valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do 
# novo salário. 
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    salario = float(input("Informe o valor do salario a receber um aumento: "))
    porc = int(input("Informe o valor da porcentagem a aumentar o salario: "))
    p = porc / 100
    a = salario * p
    aumento = salario + a
    print("o salario é de: ",salario,"R$, a porcentagem do aumento foi de: ",porc,"%, e o salario atual é de: ",aumento," R$")
    


if __name__ == '__main__':
    main()
