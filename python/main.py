from modulo import somar, multi
from classe import Funcionario

print(somar(1,2))
print(multi(1,2))
func1 = Funcionario('Aline', 'Bevilacqua', 24)
print(f'func1 bonificacao: {func1.get_bonificacao()}')
print(f'func1 nome completo: {func1.nome_completo()}')