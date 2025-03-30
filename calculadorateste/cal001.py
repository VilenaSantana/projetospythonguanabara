print("Olá sou sua amiga calculadora.")
print("Como posso lhe ajudar?")
print("Escolha o número da função que desejar:")
print("1 Adição")
print("2 Subtração")
print("3 Multiplicação")
print("4 Divisão")
funcao = int(input("Qual função deseja? "))
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
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
    print("Você selecionou divisão")
    print(f"O resultado é {n1 / n2}")
