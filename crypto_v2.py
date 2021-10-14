def cesar(frase, chave): #função cesar(data???, quantidade de caractere que vai pular,Criptografado ou Descriptografado )
    alfabeto = ' abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚ,.' # declarando alfabeto
    atualiza_frase = '' # variavel string vazia 
    for x in frase: #laço de repetição, repete a cada caractere da palavra original
        pega_numero = alfabeto.find(x) # pega_numero pega a posição de cada caractre. X separa os caracteres  
        atualiza_numero = pega_numero + chave #Pega a posição do caractere no alfabeto , e soma com a chave
        atualiza_frase = atualiza_frase + alfabeto[atualiza_numero:atualiza_numero+1] #Pula os numeros ate o caractere certo 
    return atualiza_frase #retorna frase atualizada
    
chave = int(input("Números de caracteres para pular:")) # Numeros de caracteres para pular
original = input("Escreva seu texto:") # Texto original
print('  Original:', original) # Printa o original
modo = int(input("Selecione o modo:")) # Seleciona entre criptografia ou descriptografia
if (modo == 1): 
  cifrada = cesar(original, chave) #Chama a função 
  print('Criptografado:', cifrada) #cifrada
elif(modo == 2):
  chave = chave * -1 #Deixa a chave negativa
  cifrada = cesar(original, chave) #Chama a função
  print("Descriptografado: ", cifrada) #Printa o texto descriptografado
