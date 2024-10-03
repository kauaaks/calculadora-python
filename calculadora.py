# 4 funções, mult., div., som., sub. Primeiro pedir qual operação o cliente deseja fazer
lista = []
operacao = int(input("escolha: 1-divisão; 2-multiplicação; 3-soma; 4-subtração "))
def calculadora(): 
    
    def divisao():
        try:
            resultadodadivisao= lista[0] / lista[1]
            return resultadodadivisao 
        except:
            return "ERRO: divisão por zero"
            
    def multiplicacao():
        resultadodamultiplicacao = lista[0] * lista[1]
        return resultadodamultiplicacao 
        
    def soma():
        resultadodasoma = lista[0] + lista[1]
        return resultadodasoma
        
    def subtracao():
        resultadodasubtracao = lista[0] - lista[1]
        return resultadodasubtracao 


    for i in range(2):
        num = float(input("digite o número:"))
        lista.append(num)
    if operacao == 1:
        return (divisao())
    elif operacao == 2:
        return(multiplicacao())
    elif operacao == 3:
        return(soma())
    elif operacao == 4:
        return(subtracao())
        
print (f'O Resultado é: {(calculadora())}')


    

   

   
