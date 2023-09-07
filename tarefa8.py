#1. Função sem parâmetros e sem retorno:


def boas_vindas():
    print("Bem-vindo(a) ao nosso programa!")

boas_vindas()


#2. Função com parâmetros e sem retorno:
def somar_numeros(num1, num2):
    soma = num1 + num2
    print("A soma dos números é:", soma)


somar_numeros(3, 4)


#3. Função com parâmetros e retorno:



def dobrar_numero(num):
    return num * 2

resultado = dobrar_numero(5)
print("O dobro do número é:", resultado)


