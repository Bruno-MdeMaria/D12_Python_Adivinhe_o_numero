import random
from tracemalloc import start

def num_mente():
    return random.randint(1,100)

nivel = input("Qual o nível de dificuldade você escolhe? 'Easy' ou 'Hard'?\n").lower()

if nivel == "easy":
    tentativas = 10
else: tentativas = 5

numero = num_mente()
print(numero)  #MOMMENTO

continuar = True
while continuar == True:
    palpite = int(input(f"\nVocê tem {tentativas} tentativas.\nDiga um número: "))

    if palpite != numero:
        tentativas -= 1
        if palpite > numero:
            print(f"\nO número que pensei é MENOR que {palpite}.")
        else:
             print(f"\nO número que pensei é MAIOR que {palpite}.")
        if tentativas == 0:
             continuar = False
             print("Você zerou suas tentativas. Você perdeu!")
    else: 
        continuar = False
        print("Você acertou!")   