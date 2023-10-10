
import random

def jogo_pedra_papel_tesoura():
    opcoes = ["pedra", "papel", "tesoura"]
    print('Bem-Vindo ao jogo jokenpô')
    nome = input('Digite seu nome ')
    
    while True:
        usuario_escolha = input(f"Olá {nome} escolha pedra, papel ou tesoura (ou 'sair' para encerrar): ").lower()
        if usuario_escolha == "sair":
            return  # Encerra o jogo se o usuário digitar "sair".
        elif usuario_escolha in opcoes:
            break
        else:
            print(f" {nome} Você entrou com uma escolha inválida. Tente novamente.")
    
    bot_escolha = random.choice(opcoes)
    
    print(f"Você escolheu: {usuario_escolha}")
    print(f"O bot escolheu: {bot_escolha}")

    if usuario_escolha == bot_escolha:
        print("Empate!")
    elif (
        (usuario_escolha == "pedra" and bot_escolha == "tesoura") or
        (usuario_escolha == "papel" and bot_escolha == "pedra") or
        (usuario_escolha == "tesoura" and bot_escolha == "papel")
    ):
        print("Você ganhou!")
    else:
        print("O bot ganhou!")

if __name__ == "__main__":
    while True:
        jogo_pedra_papel_tesoura()
        continuar = input("Deseja jogar novamente? (Digite 'sim' ou 'sair'): ").lower()
        if continuar == "sair":
            break 
        