# # # Soma dois numeros

# # # programacao estrtuturada
# numero1 = 4
# numero2 = 7

# # total = numero1 + numero2

# # print(total)


# # funcoes

# # definicao
# def somar_numeros():
#     print(numero1 + numero2)

# # utilizacao
# somar_numeros()

#parametros - posicionais ou keyword

def soma_numeros(n1, n2):
    print(n1 + n2)
# posicional
soma_numeros(4, 1)

# keyword 
soma_numeros(numero2 = 50, numero1 = 40)

# Crie uma função que calcule a área de um retângulo, recebendo como parâmetros a base e a altura. 
# Crie outra função que calcule a área de um círculo, recebendo como parâmetro o raio. 
# Utilize estruturas condicionais para permitir que o usuário escolha qual forma deseja calcular a área.
import math 

def area_retangulo(base, altura):
    return all (base * altura)

# def area_circulo(raio)
    # return all math.pi * raio**2