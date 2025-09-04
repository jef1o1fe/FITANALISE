#PROGRAMA PARA ACADEMIA
#menu
def menu():
    print('____________________________________')
    print('BEM VINDO A FITANALISESE')
    print('____________________________________')
    print('1-CALCULAR IMC')
    print('2-TREINO SIMPLIFICADO')
    print('0-SAIR')
def pessoas_imc():
    print('____________________________________')
    nome = input('qual seu nome: ')
    altura = float(input('qual sua altura: '))
    peso = float(input('qual seu peso: '))
    print('____________________________________')
    global imc
    imc = (peso/(altura*altura))
    print('____________________________________')
    print('OI',nome)
    print('SEU IMC:', imc)
    return imc
def classificacao_imc():
    if imc <= 18.5:
        print('sua classificação:MAGREZA')
    elif imc >=18.5 and imc <= 24.9:
        print('sua classificação:NORMAL')
    elif imc >=25 and imc <= 29.9:
        print('sua classificação:SOBREPESO')
    elif imc >=30 and imc <= 34.9:
        print('sua classificação:OBESIDADE GRAU I')
    elif imc >=35 and imc <= 39.90:
        print('sua classificação:OBESIDADE GRAU II')
    else:
        print('sua classificação:OBESIDADE GRAU III')

    print('____________________________________')
    print('IMC MENOR QUE 18.5 "MAGREZA"')
    print('IMC 18.5 A 24.9 "NORMAL"')
    print('IMC 25 A 29.9 "SOBREPESO"')
    print('IMC 30 A 34.9 "OBESIDADE GRAU I"')
    print('IMC 35 A 39.9 "OBESIDADE GRAU II"')
    print('IMC MAIOR QUE 40 "OBESIDADE GRAU III"')
    print('____________________________________')
    print('CONSULTE UM MÉDICO PARA MELHORES INFORMAÇÕES!!')
def treino():
    objetivo= int(input('QUAL SEU OBJETIVO 1-("PERDER") OU 2-("GANHAR") PESO: '))
    if objetivo ==1:
        with open("perca.txt", encoding= "UTF-8" ) as file:
            print("AQUI ESTÃO ALGUNS EXERCICIOS PARA VOCÊ PERDER PESO!!")
            print(file.read())
    elif objetivo ==2:
        with open('ganho.txt', encoding= "UTF-8") as file:
            print("AQUI ESTÃO ALGUNS EXERCICIOS PARA VOCÊ GANHAR PESO!!")
            print(file.read())
    else:
        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE!!')


while True:
    menu()
    opcao = int(input('ESCOLHA UMA OPÇÃO: '))

    if opcao ==1:
        pessoas_imc()
        classificacao_imc()
    elif opcao ==2:
        treino()
        print('VOLTE SEMPRE!!')
        
    elif opcao ==0:
        print('ATENDIMENTO FINALIZADO!!')
        break