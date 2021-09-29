crypto = 1 #Criptografado
descrypto = 0 #Descriptografado

def cesar(palavra, chave, modo): #função cesar(data???, quantidade de caractere que vai pular,Criptografado ou Descriptografado )
    alfabeto = ' abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚ,.' # declarando alfabeto
    atualiza_palavra = '' # variavel string vazia 
    for c in palavra: #laço de repetição, repete a cada caractere da palavra original
        pega_numero = alfabeto.find(c) 
        if pega_numero == -1:
            atualiza_palavra = atualiza_palavra + c
        else:
            atualiza_numero = pega_numero + chave if modo == crypto else pega_numero - chave
            atualiza_numero = atualiza_numero % len(alfabeto)
            atualiza_palavra = atualiza_palavra + alfabeto[atualiza_numero:atualiza_numero+1]
    return atualiza_palavra
    
chave = int(input("Números de caracteres para pular:"))
original = input("Escreva seu texto:")
print('  Original:', original) #original
modo = int(input("Selecione o modo:"))
if (modo == 1):
  cifrada = cesar(original, chave, crypto)
  print('Encriptada:', cifrada) #cifrada
elif(modo == 2):
  chave = chave * -1
  cifrada = cesar(original, chave, crypto)
  print("Desencriptada: ", cifrada)
  
  




