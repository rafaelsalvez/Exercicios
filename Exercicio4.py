#ponto do steak


temperatura = int(input('Para saber o pornto da carne, digite sua temperatura: '))

if  temperatura in range(48, 53):
    print('Sua carne esta rare (selada)')
elif temperatura in range(54, 59):
    print('Sua carne esta medium rare (ao ponto pra mal)')    
elif temperatura in range(60, 64):
    print('Sua carne esta medium (ao ponto)')
elif temperatura in range(65, 70):
    print('Sau carne esta medium well(ao ponto para bem)')
elif temperatura <= 47:
    print('Sua carne está crua.')
else:
    print('Sua carne esta well done ( bem passsada)')