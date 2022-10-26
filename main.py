# comando input():quero permitir que o usuario digite algo

nome = input("digite seu nome: ")
#pede a idade para o usuario "qual sua idade?"
idade = int(input("qual sua idade?: "))

#comando de saida...exibir na tela
print(f"seu nome é {nome}")

#exiba "sua idade é"
print("sua idade é {}".format(idade))

#se quiser mostrar o dobro da idade informada
double=idade*2
print("o dobro da idade informada é {}".format(double))