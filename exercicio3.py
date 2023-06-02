for i in range(1000, 2001):
    if i % 11 == 5:
        print(i)

# ----------------------------------------------------------------------------------------------------------------------------------------------------#

for i in range(1, 11):
    print("Tabuada do", i)
for j in range(1, 11):
    print(i, "x", j, "=", i*j)

# ----------------------------------------------------------------------------------------------------------------------------------------------------#

amigos = ["João", "Maria", "Carlos", "Ana"]


for amigo in amigos:
    print(amigo)

# ----------------------------------------------------------------------------------------------------------------------------------------------------#


def soma(a, b):
    return a + b


def subtrai(a, b):
    return a - b


def multiplica(a, b):
    return a * b


def divida(a, b):
    return a / b


while True:
    print("Escolha uma operação")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")

    escolha = input("Escolha uma: 1/2/3/4: ")

    if escolha in ('1', '2', '3', '4'):
        num1 = float(input("Digite um número: "))
        num2 = float(input("Digite outro número: "))

        if escolha == '1':
            print(num1, "+", num2, "=", soma(num1, num2))

        elif escolha == '2':
            print(num1, "-", num2, "=", subtrai(num1, num2))

        elif escolha == '3':
            print(num1, "x", num2, "=", multiplica(num1, num2))

        elif escolha == '4':
            print(num1, "/", num2, "=", divida(num1, num2))

            break
        else:
            print("Erro! Tente novamente.")

# ----------------------------------------------------------------------------------------------------------------------------------------------------#

amigos = ["João", "Maria", "Carlos", "Ana"]


for amigo in amigos:
    saudacao = f"Olá, {amigo}! Como vai você?"
    print(saudacao)

# ----------------------------------------------------------------------------------------------------------------------------------------------------#

convidados = ["Leonardo DiCaprio", "Beyoncé",
              "Dwayne Johnson", "Emma Watson", "Tom Hanks"]


def enviar_convite(nome):
    mensagem = f"Olá, {nome}! Gostaríamos de convidá-lo(a) para um jantar em nossa casa. Será uma noite incrível! Esperamos contar com sua presença. Atenciosamente, Anfitriões."
    print(f"Enviando convite para: {nome}")
    print(mensagem)
    print()


for convidado in convidados:
    enviar_convite(convidado)

celebridade_indisponivel = "Emma Watson"

print(f"{celebridade_indisponivel} não poderá comparecer ao jantar.")
print()

novo_convidado = "Jennifer Lawrence"
convidados[convidados.index(celebridade_indisponivel)] = novo_convidado

for convidado in convidados:
    enviar_convite(convidado)

# ----------------------------------------------------------------------------------------------------------------------------------------------------#

usuarios = []


def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    email = input("Digite o email do usuário: ")

    usuario = {"nome": nome, "idade": idade, "email": email}
    usuarios.append(usuario)


for _ in range(3):
    cadastrar_usuario()

print("Usuários cadastrados:")
for usuario in usuarios:
    print(f"Nome: {usuario['nome']}")
    print(f"Idade: {usuario['idade']}")
    print(f"Email: {usuario['email']}")
    print()
