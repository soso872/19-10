# comando input():quero permitir que o usuario digite algo

nome = input("digite seu nome:\n ")
#pede a idade para o usuario "qual sua idade?"
idade = int(input("qual sua idade?:\n "))

#comando de saida...exibir na tela
print(f"seu nome é\n {nome}")

#exiba "sua idade é"
print("sua idade é\n {}".format(idade))

#se quiser mostrar o dobro da idade informada
double=idade*2
print("o dobro da idade informada é {}\n".format(double))

#estrutura condicional- o famoso "SE" (if)
#se a pessoa for maior de idade, mostre 'voce é maior de idade, pode dirigir e enche a cara(NÃO AO MESMO TEMPO)'

if (idade >=18):
  print("voce é maior de idade, pode dirigir ou beber\n")
else:
  print("voce não pode, é DE MENOR AINDA\n")
  
#e se eu quisesse perguntar o genero(M=masculino e F=feminino)
#mostre(...e voce tambem precisa/precisou prestar o serviço militar obrigatorio)

genero=input("informe qual é o seu gênero f= fem m=masc o=outros:\n ")
print(f"seu gênero é:\n {genero}")
 
if idade >=18 and genero == "masc":

 print("...e voce tambem precisa/precisou prestar o serviço militar obrigatorio\n")



  


print("vai ser executada de qualquer jeito\n")