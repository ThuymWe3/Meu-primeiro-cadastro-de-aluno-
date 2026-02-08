# programa de cadastro de aluno e onde o aluno sabe se foi aprovado ou reprovado . 
nome= input("Escreva seu nome completo:") #captura o nome digirado . identifica o aluno
escola= input("Nome da Escola emque estuda: ") #caputa identificação da escola 
idade =int(input("Sua idade:")) # capitura idade do aluno 
nota = float(input("digite sua nota:")) # recebe nota , e decimal Ex: 1,2,.03,5
media = 7 # define a regra minima de aprovação (regras do escola)

if nota >= media:
    
     print("Aprovado!") #executa se a condição for verdadeira 

else: 
    
     print("Reprovado!")# executa se a condição for falsa 


