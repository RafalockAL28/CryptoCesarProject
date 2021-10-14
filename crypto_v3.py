def start():    
  
  chave,original, modo = dados()

  if (modo == 1): 
    executa_cifrada(original,chave)
  elif(modo == 2):
    executa_decifrada(chave,original)
  else:
    print("Selecione um dos modos")

def dados():
  chave = int(input("Escolha seu modo de criptografia (1,2 ou 3):")) # Numeros de caracteres para pular
  original = input("Escreva seu texto:") # Texto original
  print('  Original:', original) # Printa o original
  modo = int(input("Selecione 1 para criptografar ou 2 para descriptografar:")) # Seleciona entre criptografia ou descriptografia
  return [chave, original, modo]

def executa_cifrada(original,chave):
  cifrada = cesar(original, chave) #Chama a função 
  print('Criptografado:', cifrada) #cifrada

def executa_decifrada(chave,original):
  chave = chave * -1 #Deixa a chave negativa
  cifrada = cesar(original, chave) #Chama a função
  print("Descriptografado: ", cifrada) #Printa o texto descriptografado

def cesar(frase, chave): 
    alfabeto = ' abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚ,.0123456789' # declarando alfabeto
    atualiza_frase = '' # variavel string vazia 
    for x in frase: #laço de repetição, repete a cada caractere da palavra original
        pega_numero = alfabeto.find(x) # pega_numero pega a posição de cada caractre. X separa os caracteres  
        atualiza_numero = pega_numero + chave #Pega a posição do caractere no alfabeto , e soma com a chave
        atualiza_numero = atualiza_numero % len(alfabeto) #Limita os caracteres 
        atualiza_frase += alfabeto[atualiza_numero:atualiza_numero+1] #Pula os numeros ate o caractere certo 
    return atualiza_frase #retorna frase atualizada


start()




# O OBJETIVO:
  # MODO 2 a criptografia agora é outra.
  # MODOS
    #MODO 1 Criptografia alterando um caractere chave 3
    #MODO 2 Criptografia alterando dois caracteres porra chave 5 8
    #MODO 3 Acho q vc ja entendeu ne? chave 2 7 4
    #Excluir Numeros de caractere para pular
    #Se for a chave 1
      # função cesar irá rodar uma vez com a chave 3
    #Se for a chave 1
      # função cesar irá rodar uma vez com a chave 3
      