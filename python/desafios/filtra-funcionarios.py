funcionarios = {'Ana', 'Marcos', 'Alice',
                'Pedro', 'Sophia', 'Bruno', 'Melissa'}
turno_dia = {'Ana', 'Marcos', 'Alice', 'Melissa'}
turno_noite = {'Pedro', 'Sophia', 'Bruno'}
tem_carro = {'Marcos', 'Alice', 'Bruno', 'Melissa'}

tem_carro_turno_dia = list(tem_carro.intersection(turno_dia))
print(tem_carro_turno_dia)
tem_carro_turno_noite = list(tem_carro.intersection(turno_noite))
print(tem_carro_turno_noite)
nao_tem_carro = list(funcionarios.difference(tem_carro))
print(nao_tem_carro)
