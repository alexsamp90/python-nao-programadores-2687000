ano_nascimento = 1989
ano_formatura = 2010

# Considerando que as variáveis acima correspondem a 'Gerlaine', descubra a idade dela no ano da sua formatura
idade = ano_formatura - ano_nascimento
print(idade)
# Escreva expressões comparativas usando os operadores relacionais >, <= e ==. Imprima na tela as respostas
print(ano_formatura < ano_nascimento)
print(ano_nascimento == ano_formatura - idade)

# Crie expressões comparativas mais complexas utilizando operadores lógicos and, or e not. Imprima na tela as respostas
print(idade < 20 and ano_formatura > 1990)
print(idade < 22 or ano_formatura > 1990)