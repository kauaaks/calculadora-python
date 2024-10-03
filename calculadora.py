#4 funções, mult., div., som., sub. Primeiro pedir qual operação o cliente deseja fazer
def calculadora(): 
    operacao = int(input("escolha: 1-divisão; 2-multiplicação; 3-soma; 4-subtração "))
    lista = []
    for i in range(2):
        num = float(input("digite o número:"))
        lista.append(num)
        if operacao == 1:
            return divisao
            print(f"O resultado da sua Divisão é {divisao()}")
        if operacao == 2:
            return multiplicacao
            print(f"O resultado da Multiplicação é {multiplicacao()}")
        if operacao == 3:
            return soma
            print(f"O resultado da soma é {soma()}")
        if operacao == 4:
            return subtracao
            print(f"O resultado da subtração é {subtracao()}")
        return calculadora()
print(calculadora())

    
def subtracao():
    sub = lista[0] - lista[1]
    return sub
    

   
