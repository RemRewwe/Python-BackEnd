acesso = int(input("Digite seu Numero de Acesso: "))
if acesso == 3:
    print("Acesso Total")
elif acesso == 2:
    print("Acesso Parcial")
else:
    print("Acesso Negado")



temperatura = int(input("Qual a Temperatura Presente?:"))
fahrenheit = (temperatura * 9/5) + 32
print("Temperatura em Fahrenheit:", fahrenheit)