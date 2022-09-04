#Cálculo de IMC


Altura = float(input('Digite sua altura: '))
Peso = float(input('Digite seu peso: '))
Altura = Altura * 2

indice = Peso / Altura

if indice <= 18.5:
    print('Seu indice é de Magreza! ')

elif indice >= 18.6 and indice < 25:
    print('Seu indice esta normal. ')

elif indice >= 25 and indice < 30:
    print('Seu indice é de sobrepeso. ')

elif indice >= 30.1 and indice < 40:
    print('Seu indice é de obesidade. ')
#elif indice == 30.1 a (igual)
else:
    print('Seu indice é obesidade grave, procure um médico! ')