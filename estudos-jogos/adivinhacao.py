import random

def jogar():

    print("*****************************************")
    print("*** Bem vindo ao jogo de Adivinhação! ***")
    print("*****************************************")

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if nivel == 1:    total_de_tentativas = 20
    elif nivel == 2:  total_de_tentativas = 10
    else:             total_de_tentativas = 5

    pontuacao = 1000

    numero_secreto = random.randrange(1,101)
    acertou = False

    for rodada in range(1, total_de_tentativas + 1):
        print(10 * "-")
        print("Tentativa {0} de {1}".format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu número: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou com {} tentativa(s)!".format(rodada))
            break
        elif (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

        pontuacao = pontuacao - chute

    if (not acertou):
        print("O número correto era: {0}".format(numero_secreto))

    print("Fim do jogo! Pontuação final: {0}".format(pontuacao))

if (__name__ == "__main__"):
    jogar()