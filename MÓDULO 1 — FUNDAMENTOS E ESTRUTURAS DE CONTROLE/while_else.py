#O else do while é executado quando o laço termina normalmente (sem usar break).
i = 0

while i < 3:
    print(i)
    i += 1
else:
    print("Loop terminou normalmente")

#com break
i = 0

while i < 3:
    print(i)
    if i == 1:
        break
    i += 1
else:
    print("Loop terminou normalmente")

#ambos
numeros = [1, 3, 5, 7]

for n in numeros:
    if n == 2:
        print("Encontrado")
        break
else:
    print("Não encontrado")