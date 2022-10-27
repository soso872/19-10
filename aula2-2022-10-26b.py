#pede o nome do aluno e sua nota (de 0 a 10)e,se ele tirar nota 10,mostra "VENCEMO"
nome=input("aluno(a),informe seu nome:\n")
nota= float(input("digite sua nota:\n"))

if nota==10:
  print(f"{nota},VENCEMO")

elif(nota >= 6 and nota <10):
 print(f"{nome},ta na media ok")
  
else: #é sempre o que as duas condiçoes de cima não trataram
  
  print("UUUU,sem dez pra você")
           