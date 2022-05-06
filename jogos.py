import forca
import adivinhacao

def escolhe_jogo():
    print("------------------------------------------------------------")
    print("BEM-VINDO! PARA COMEÇAR A JOGAR, SELECIONE O JOGO DESEJADO:")
    print("------------------------------------------------------------")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando opção 1 forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando opção 1 adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
