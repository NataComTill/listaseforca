num = float(input("Digite um número: "))

if num > 10:
    print("O seu número", num, "é maior que 10")
else:
    print("O seu número", num, "é menor que 10")

#----------------------------------------------------------------------------------------------------------------------------------------------------#

num = float(input("Digite um número: "))

if num < 0:
    print("Seu número é negativo")
else:
    print("Seu número é positivo")

#----------------------------------------------------------------------------------------------------------------------------------------------------#

maças = int(input("Quantas maçãs você vai comprar? "))

if maças >= 12:
    valor = maças * 1
    print("O valor será de ", valor, "R$")
else:
    valor2 = maças * 1.3
    print("O valor será de ", valor2, "R$")

#----------------------------------------------------------------------------------------------------------------------------------------------------#

nota1 = float(input("Qual a primeira nota? "))
nota2 = float(input("Qual a segunda nota? "))

media = (nota1 + nota2) / 2

if media >= 6:
    print("Sua média foi ", media, "logo você passou!")
else:
    print("Sua média foi ", media, "logo você reprovou!")

#----------------------------------------------------------------------------------------------------------------------------------------------------#

num1 = float(input("Diga um número: "))
num2 = float(input("Diga outro número: "))

while num1 == num2:
    print("Os números são iguais. Digite outro número diferente de", num1)
    num2 = float(input("Diga outro número: "))
    break
if num1 > num2:
    print("o número", num1, "é maior que", num2)
else:
    print("o número", num2, "é maior que", num1)
    
#----------------------------------------------------------------------------------------------------------------------------------------------------#

num1 = float(input("Diga um número: "))
num2 = float(input("Diga outro número: "))

while num1 == num2:
    print("Os números são iguais. Digite outro número diferente de", num1)
    num2 = float(input("Diga outro número: "))
    break
if num1 > num2:
    print(num2, num1)
else:
    print(num1, num2)

#----------------------------------------------------------------------------------------------------------------------------------------------------#

conta = int(input("Digite o número da conta: "))
saldo = float(input("Digite o saldo da conta: "))
debito = float(input("Digite o débito da conta: "))
credito = float(input("Digite o crédito da conta: "))

saldoatual = saldo - debito + credito

if saldoatual > 0:
    print("Seu saldo da conta", conta, "é", saldoatual, "logo é positivo!")
else:
    print("Seu saldo da conta", conta, "é", saldoatual, "logo é negativo!")

#----------------------------------------------------------------------------------------------------------------------------------------------------#

quantidadeatual = int(input("Qual a quantidade atual do estoque? "))
quantidademaxima = float(input("Qual a quantidade máxima do estoque? "))
quantidademinima = float(input("Qual a quantidade mínima do estoque? "))

quantidademedia = (quantidademaxima + quantidademinima) / 2

if quantidadeatual >= quantidademedia:
    print(quantidademedia, "logo, não efetuar compra.")
else:
    print(quantidademedia," logo, efetuar compra.")

#----------------------------------------------------------------------------------------------------------------------------------------------------#

nota1 = float(input("Qual a primeira nota? "))
nota2 = float(input("Qual a segunda nota? "))

notamedia = (nota1 + nota2) / 2

if notamedia < 4:
    print("(E)")
    print("Sua média foi", notamedia, ", assim você está reprovado")
elif notamedia >= 4 and notamedia < 6:
    print(("D"))
    print("Sua média foi", notamedia, ", assim você está reprovado")
elif notamedia >= 6 and notamedia < 7.5:
    print(("C"))
    print("Sua média foi", notamedia, ", assim você está aprovado")
elif notamedia >= 7.5 and notamedia < 9:
    print(("B"))
    print("Sua média foi", notamedia, ", assim você está aprovado")
elif notamedia >= 9:
    print(("A"))
    print("Sua média foi", notamedia, ", assim você está aprovado")
