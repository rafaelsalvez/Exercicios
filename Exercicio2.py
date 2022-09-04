#Tabela de funcionários

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sofia', 'Buno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sofia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

s1 = set(turno_noite)
s2 = set(tem_carro)
s3 = set(turno_dia)
s4 = set(funcionarios)

print(f'Quem trabalha a noite e tem carro: {s1 & s2}')

print(f'Quem trabalha de dia e tem carro: {s2 & s3}')

print(f'Quem não tem carro: {s4 - s2}')