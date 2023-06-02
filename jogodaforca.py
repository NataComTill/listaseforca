import random

# Lista de temas e palavras
temas = {
    "frutas": ["banana", "abacaxi", "uva"],
    "animais": ["gato", "cachorro", "elefante"],
    "países": ["brasil", "canadá", "austrália"],
    "nomes": ["natã", "ian", "zayon"],
    "Jogos": ["forza", "lol", "minecraft"]

}

tema = random.choice(list(temas.keys()))

palavra = random.choice(temas[tema])

letras_erradas = []

boneco_forca = [
    "  O",
    " /",
    " |",
    " /",
    " |"
]

palavra_oculta = ["_"] * len(palavra)


def imprimir_forca():
    for linha in boneco_forca:
        print(linha)


def imprimir_palavra_oculta():
    print("Palavra:", " ".join(palavra_oculta))


while True:

    print("\n" * 100)

    imprimir_forca()

    imprimir_palavra_oculta()

    print("Letras erradas:", ", ".join(letras_erradas))

    letra = input("Digite uma letra: ").lower()

    if letra in letras_erradas or letra in palavra_oculta:
        print("Você já jogou essa letra antes. Tente outra.")
        continue

    if letra in palavra:

        for i, char in enumerate(palavra):
            if char == letra:
                palavra_oculta[i] = letra
    else:

        letras_erradas.append(letra)

        if len(letras_erradas) == len(boneco_forca):
            # Limpar a tela
            print("\n" * 100)

            imprimir_forca()

            print("Você perdeu! A palavra correta era:", palavra)
            break

    if "_" not in palavra_oculta:

        print("\n" * 100)

        imprimir_forca()

        print("Parabéns! Você ganhou!")
        break
