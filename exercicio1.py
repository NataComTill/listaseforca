metros = float(input("Digite os metros: "))

centimetros = metros * 100

print(centimetros)

#----------------------------------------------------------------------------------------------------------------------------------------------------#

raio = float(input("Digite o raio: "))

área = raio ** 2 * 3.14

print(área)

#----------------------------------------------------------------------------------------------------------------------------------------------------#

lado1 = float(input("Digite o lado: "))
lado2 = float(input("Digite o 2° lado: "))

Área = lado1 * lado2
resultado = Área * 2

print(resultado)

#----------------------------------------------------------------------------------------------------------------------------------------------------#

salarioporhora = float(input("Quanto você ganha por hora? "))
horas = float(input("Por quantas horas no mês? "))

salario = salarioporhora * horas

print(salario)

#----------------------------------------------------------------------------------------------------------------------------------------------------#

temperaturaF = float(input("Digite a temperatura em Fahrenheit: "))

temperaturaC = 5 * ((temperaturaF-32) / 9)

print(temperaturaC)

#----------------------------------------------------------------------------------------------------------------------------------------------------#

temperaturaC = float(input("Digite a temperatura em Celsius: "))

temperaturaF = (temperaturaC * 9/5) + 32

print(temperaturaF)

#----------------------------------------------------------------------------------------------------------------------------------------------------#

numero1 = int(input("Digite o número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero3 = float(input("Digite o número real: "))

ex1 = numero1 * 2 * (numero2 / 2)
ex2 = numero1 * 3 + numero3
ex3 = numero3 ** 3

print(ex1)
print(ex2)
print(ex3)

#----------------------------------------------------------------------------------------------------------------------------------------------------#

altura = float(input("Digite o altura: "))

pesoideal =  72.7 * altura - 58

print(pesoideal)

#----------------------------------------------------------------------------------------------------------------------------------------------------#

genero = input("Qual seu gênero, homem ou mulher? ")
altura = float(input("Digite a altura em metros: "))

if genero == "homem":
    pesoidealH = (72.7 * altura) - 58
    print(pesoidealH)
else:
    pesoidealM = (62.1 * altura) - 44.7
    print(pesoidealM)


