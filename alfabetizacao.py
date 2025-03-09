import random

# Lista de palavras e dicas
palavras = [
    ("Abacaxi", "Fruta tropical amarela e espinhosa"),
    ("Banana", "Fruta amarela e curva"),
    ("Cavalo", "Animal usado para montar"),
    ("Dado", "Objeto usado em jogos de tabuleiro"),
    ("Elefante", "Maior animal terrestre"),
    ("Foca", "Animal que vive tanto na água quanto na terra"),
    ("Gato", "Animal de estimação comum, adora caçar ratos"),
    ("Hipopótamo", "Animal grande e pesado que vive em rios"),
    ("Igreja", "Lugar de culto religioso"),
    ("Jacaré", "Réptil grande que vive em rios e pântanos"),
]

def jogo_alfabetizacao():
    print("Bem-vindo ao Jogo de Alfabetização!")
    print("Você terá que identificar a letra correta com base na dica fornecida.\n")

    # Seleciona uma palavra aleatória
    palavra, dica = random.choice(palavras)
    letra_correta = palavra[0].upper()

    print(f"Dica: {dica}")
    print(f"Qual é a primeira letra da palavra?\n")

    # Solicita a resposta do jogador
    resposta = input("Digite a letra: ").upper()

    if resposta == letra_correta:
        print("Parabéns! Você acertou!")
    else:
        print(f"Que pena! A resposta correta é '{letra_correta}'.")

if __name__ == "__main__":
    jogo_alfabetizacao()
