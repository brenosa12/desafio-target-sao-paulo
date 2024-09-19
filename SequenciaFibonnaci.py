def verificar_numero(numero):
    x = 0
    y = 1
    pertence = False

    if numero == x or numero == y:
        pertence = True

    proximo = x + y

    while proximo <= numero:
        if proximo == numero:
            pertence = True
        x = y
        y = proximo
        proximo = x + y

    return pertence


if __name__ == "__main__":
    numero = int(input("Informe um número: "))

    if verificar_numero(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
