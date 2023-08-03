import random as r

print("*********************")
print(" Jogo da adivinhacao ")
print("*********************")

numero_secreto = int(r.randrange(1, 101)) # A função random.random gera um numero entre 0.0 e 1.0
rodada = 1

print("Escolha um nível de dificuldade: \n")
print("1 - Facil: 15 tentativas\n")
print("2 - Medio: 10 tentativas\n")
print("3 - Dificil: 5 tentativas\n")
nivel = int(input("Digite o numero equivalente a dificuldade escolhida: \n"))

while nivel < 1 or nivel > 3:
    print("NIVEL ESCOLHIDO INVALIDO. DEVE SER ENTRE 1 E 3.\n")
    print("Escolha um nível de dificuldade: \n")
    print("1 - Facil: 15 tentativas\n")
    print("2 - Medio: 10 tentativas\n")
    print("3 - Dificil: 5 tentativas\n")
    nivel = int(input("Digite o numero equivalente a dificuldade escolhida: \n"))

if nivel == 1:
    total_tentativas = 15
elif nivel == 2:
    total_tentativas = 10
else:
    total_tentativas = 5

for rodada in range(1, total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute = int(input("Digite o seu chute de 1 a 100\n"))

    while chute < 1 or chute > 100:
        print("Você deve chutar um número entre 0 e 100...")
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute = int(input("Digite o seu chute de 0 a 100\n"))

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Voce acertou! Parabens!")
        break
    else:
        if maior:
            print("O numero digitado eh maior que o numero secreto...")
        elif menor:
            print("O numero digitado eh menor que o numero secreto...")

    if not acertou:
        print("Acabaram suas chances e voce perdeu...")

print("Fim de jogo")
