prossiga = str(input("deseja continuar: (sim/não):")).lower()
while prossiga == 'sim':

    def eh_polindromo (palavra):
        return palavra == palavra[::-1]

    palavra_digitada = str(input("digite a palavra para ver se ela é políndromo: "))

    if eh_polindromo(palavra_digitada):
        print(f"a palavra {palavra_digitada} é políndromo")
    else:
        print(f"a palavra {palavra_digitada} não é políndromo")

    prossiga = str(input("deseja continuar: (sim/não):")).lower()
print("----------------------programa finalizado-----------------------------")


