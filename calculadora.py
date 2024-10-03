#4 funções, mult., div., som., sub. Primeiro pedir qual operação o cliente deseja fazer
def divisao():
    try:
        div= lista[0] / lista[1]
        return div
    except:
        return "ERRO: divisão por zero"
        
def multiplicacao():
    mult = lista[0] * lista[1]
    return mult
    
def soma():
    som = lista[0] + lista[1]
    return som
    
def subtracao():
    sub = lista[0] - lista[1]
    return sub

operacao = int(input("escolha: 1-divisão; 2-multiplicação; 3-soma; 4-subtração "))
lista = []
def calculadora(): 

    for i in range(1):
        num = float(input("digite o número:"))
        lista.append(num)
    if operacao == 1:
        print(f"O resultado da sua Divisão é {divisao()}")
    elif operacao == 2:
        print(f"O resultado da Multiplicação é {multiplicacao()}")
    elif operacao == 3:
        print(f"O resultado da soma é {soma()}")
    elif operacao == 4:
        print(f"O resultado da subtração é {subtracao()}")
    return calculadora()
print(calculadora())



    

   

   
