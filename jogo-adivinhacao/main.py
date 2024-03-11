import random   

    

def jogo_adivinhacao():

    numero_secreto = random.randint(1, 100)



    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100.")

    tentativas = 0
    while tentativas == 0:
        Dificuldade = int(input("Selecione a dificuldade: \n 1-Fácil \n 2-Médio \n 3-Dificil \n"))
    
        if Dificuldade == 1:
            tentativas = 10
            

        elif Dificuldade == 2:
            tentativas = 7
            

        elif Dificuldade == 3:
            tentativas = 4
        
        else:
            print("Tente Novamente")


    print(f"Você tem {tentativas} tentativas.")
        
    while tentativas > 0:
        chute = int(input("Digite seu chute: "))

        if chute < numero_secreto:
            print("O número secreto é maior.")
        elif chute > numero_secreto:
            print("O número secreto é menor.")
        else:
            print("Parabéns! Você acertou!")
            return

        tentativas -= 1
        if tentativas > 0:
            print(f"Você tem mais {tentativas} tentativas.")

    print("Suas tentativas acabaram. O número secreto era:", numero_secreto)


jogo_adivinhacao()
