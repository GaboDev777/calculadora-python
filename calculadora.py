numero1 = int(input("Inserir o primeiro numero: "))
operacao = int(input("Escolha a operação a ser realizada: \n 1: + \n 2: - \n 3: * \n 4: / \n Num: "))
numero2 = int(input("Inserir o segundo numero: "))

if operacao == 1:
    resultado =  numero1 + numero2

elif operacao == 2:
    resultado =  numero1 - numero2

elif operacao == 3:
    resultado =  numero1 * numero2

elif operacao == 4:
    if numero2 == 0:
        resultado = "Erro"
    else:
        resultado = numero1 / numero2

else:
    resultado = "Operação inválida."


print("Resultado:", resultado)
