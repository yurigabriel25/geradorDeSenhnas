import random 

print('Be-vindo ao seu gerador de senha.')

cont = input('Para que serviço ou conta você uer gerar senha? ')

print('Você está gerando senha para',cont)

chaves = ('abcdefghijlmnopqrstuvwxyzABCDEFGHIJLMNOPQRSTUVWXYZ12345678910!@#$%&*')

num = int(input('Quatas senhas você quer montar? '))

comp = int(input('Qual vai ser o comprimento da sua senha? '))

print('As seguintes senhas foram geradas:')


for sen in range(num):
    senhas = ''
    for c in range(comp):
        senhas += random.choice(chaves)
    print(senhas)
    

    
        

