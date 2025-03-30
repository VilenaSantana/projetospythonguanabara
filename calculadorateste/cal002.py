# Corrigindo falhas do cal001
from selectors import SelectSelector

print("Olá sou sua amiga calculadora.")
print("                            ")
print("Como posso lhe ajudar?")
print("                            ")
print("Escolha o número da função que desejar:")
print("                            ")
print("1 Adição")
print("2 Subtração")
print("3 Multiplicação")
print("4 Divisão")
print("                            ")
# verificando se a função escolhida é valida com laço de repetição
while True:
    funcao = int(input("Qual função deseja? "))
    print("                            ")
    if funcao < 1 or funcao > 4:
        print("Opção invalida, por favor digite uma dessas opções: ")
        print("                            ")
        print("1 Adição")
        print("2 Subtração")
        print("3 Multiplicação")
        print("4 Divisão")
        print("                            ")
    else:
        break
# sendo escolhido um número valido vamos para o calculo
n1 = float(input("Digite o primeiro número: "))
print("                            ")
n2 = float(input("Digite o segundo número: "))
print("                            ")
if funcao == 1:
    print("Você selecionou adição")
    print(f"O resultado é {n1 + n2}")
elif funcao == 2:
    print("Você selecionou subtração")
    print(f"O resultado é {n1 - n2}")
elif funcao == 3:
    print("Você selecionou multiplicação")
    print(f"O resultado é {n1 * n2}")
elif funcao == 4:
    if n2 != 0:  # Verifica se o segundo número não é zero para evitar divisão por zero
        print("Você selecionou divisão")
        print(f"O resultado é {n1 / n2}")
    else:
        print("Erro: Não é possível dividir por zero.")
