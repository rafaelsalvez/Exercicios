#calculos de tinta

rend_tinta = float(input('Qual o rendimento da lata? '))
altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))

def rendimento():
    num1 = altura
    num2 = largura
    num3 = rend_tinta
    rend = num1 + num2 / num3
    print(f'Voce vai precisar de {rend} latas de tinta!!')

rendimento()