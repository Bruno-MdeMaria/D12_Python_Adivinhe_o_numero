import random
from art import logo

def num_mente():
    return random.randint(1,100)
def dificuldade():    #UTILIZANDO GLOBAL SCOPE
    nivel = input("Qual o nível de dificuldade você escolhe? 'Easy' ou 'Hard'?\n").lower()
    if nivel == "easy":
        return TENTATIVAS_EASY
    else: return TENTATIVAS_HARD

TENTATIVAS_EASY = 10      #GLOBAL SCOPE - FORMA DE UTILIZAR GLOBAL SCOPE. VALORES QUE NÃO SE ALTERAM. EASY SEMPRE SERÁ 5 E HARD 10.
TENTATIVAS_HARD = 5

print(logo)
print("\nBem vindo ao jogo Adivinhe o Número!")
print("Estou pensando em número de 1 a 100. Tente adivinhar!")



numero = num_mente()
#print(numero)  #TEMP

continuar = True
tentativas = dificuldade()
while continuar == True:
    
    palpite = int(input(f"\nVocê tem {tentativas} tentativas.\nDiga um número: "))

    if palpite != numero:
        tentativas -= 1
        if palpite > numero:
            print(f"\nO número que pensei é MENOR que {palpite}.🙃")
        else:
             print(f"\nO número que pensei é MAIOR que {palpite}.😁")
        if tentativas == 0:
             continuar = False
             print("Você zerou suas tentativas.😱\nVocê perdeu!😭")
    else: 
        continuar = False
        print("Você acertou!😎")   