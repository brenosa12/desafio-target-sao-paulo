def inverterString(palavra):
    nova_palavra = ""

    if len(palavra) > 1:
        for i in range(len(palavra)-1, -1, -1):
            nova_palavra += palavra[i]
    
        return nova_palavra
    else:
        return palavra

   

if __name__ == "__main__":
    palavra = input("Informe a string: ")

    print(inverterString(palavra))
