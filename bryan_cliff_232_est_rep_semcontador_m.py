# -*- coding: utf-8 -*-
"""Bryan Cliff - 232_Est_Rep_SemContador_m.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OGI9ZRh4CCArMrUsdScKm3zCX7ugs26X

# **EXERCÍCIOS DE ESTRUTURA DE REPETIÇÃO SEM CONTADOR**

###1. Construir um algoritmo para calcular e apresentar o total de salários pagos de funcionários, mas não é informado a quantidade de pessoas, então use como critério de parada (condição da estrutura de repetição, digitar zero no salário para sair.
"""



total_salarios = 0     #começa de 0 poís ainda não foi pago nenhum salário
salario = float(input('Digite aqui o salário, (digite 0 para sair): '))
while salario > 0:
    total_salarios = total_salarios + salario
    salario = float(input('Digite o salário: '))
print(f'Total de salário pagos R$ {total_salarios:.2f}')

"""###2. Faça um programa que receba a altura de **5 pessoas**. Encontre e apresente a altura da pessoa mais alta e da mais baixa e seus respectivos nomes."""

for pessoas in range(5):
    altura = float(input('Informe a altura: '))
    nome = input('Informe o nome: ')
    # dica de implementação, inicializar as variáveis de menor e maior
    # valor dentro do laço de repetição, quando você souber, quantas
    # vezes repete
    if pessoas == 0:
        alto = altura
        nomea = nome
        baixo = altura
        nomeb = nome
    if altura >= alto:
        alto = altura
        nomea = nome
    elif altura <= baixo:
        baixo = altura
        nomeb = nome
print(nomea,'é mais alto, com',alto,'metros')
print(nomeb,'é mais baixo, com',baixo,'metros')

"""###3. Faça um programa que receba a altura de **várias pessoas**. Encontre e apresente a altura da pessoa mais alta e da mais baixa e seus respectivos nomes. Para encerrar a entrada de dados, zero na altura, mas esta não poderá ser considerada como resposta da altura da pessoa mais baixa.

"""

print('Para parar a contagem digite 0 na altura')
altura = float(input('Didite a altur........:'))
alto = altura
baixo = altura
while altura > 0:
    nome = input('Digite o nome: ')
    if altura >= alto:
        alto = altura
        nome_alto = nome
    if altura <= baixo:
        baixo = altura
        nome_baixo = nome
    altura = float(input('Digitre a altura: '))
print(f'Nome alto: {nome_alto} altura {alto} mt')
print(f'Nome baixo: {nome_baixo} altura {baixo} mt')

"""###4. Faça um programa que receba a idade e a altura de **várias pessoas**. Calcule e exiba a média das alturas das pessoas com mais de 20 anos. Para encerrar a entrada de dados, digite uma idade negativa ou igual a zero.



"""

# Digite seu código aqui
media = 0
contAltura = 0
media_1 = 0
print('Para parar a contagem digite 0 na idade e depois na altura')
idade = int(input('digite um numero para inicio do programa.....: '))
while idade > 0:
  idade = int(input('digite a idade: '))
  altura = float(input('digite a altura: '))
  if idade > 20:
    media = media + altura
    contAltura = contAltura + 1
    media_1 = (media / contAltura)
print('A media das alturas das pessoas maiores que 20 anos é: ', media_1)

"""###5. Construir um algoritmo para calcular e apresentar a idade atual de **algumas pessoas** em relação ao ano atual, mas não é informado a quantidade de pessoas, então use como critério de parada (condição da estrutura de repetição, digitar zero no ano de nascimento para sair."""

# Digite seu código aqui
idade_atual = 0
print('digite 0 para parar a contagem')
ano_nascimento = int(input('digte o ano de nascimento: '))
while ano_nascimento > 0:
  ano_atual = int(input('Digite o ano atual: '))
  idade_atual = ano_atual - ano_nascimento
  print(f"A idade atual é {idade_atual} anos.")
  ano_nascimento = int(input('Digite o ano de nascimento ou 0 para encerrar: '))

"""###6. Faça um programa que **vários valores inteiros**, calcule e exiba o maior e o menor valor do conjunto.

*   Para encerrar a entrada de dados, deve ser digitado o valor zero;
*   Para valores negativos, deve ser enviada uma mensagem;
*   Esses valores (zero e negativos) não entrarão na lógica de encontrar o maior e o menor valor.


"""

valor = int(input('Digite um valor inteiro (digite zero para sair..): '))
maior = valor
menor = valor
while valor != 0: # a)
    if valor < 0: # b)
        print('Valor digitado é negativo')
    if valor > maior:
        maior = valor
    if valor < menor and valor > 0:
        menor = valor
    valor = int(input('Digite um valor inteiro (digite zero para sair): '))
print(f"Maior valor encontrado: {maior}")
print(f"Menor valor encontrado: {menor}")

"""###7. No final do ano **muitas pessoas** compram presentes. Para identificar o perfil dos compradores numa loja de roupas, faça um programa que registre os dados de algumas pessoas, pergunte “Deseja cadastrar outro (‘**s**’/’n’)?”. Enquanto a resposta for **s** repete, quando for n encerra e repetição e apresente os seguintes resultados:
a) Quantidade de pessoas de gênero **f** - feminino e **m** - mesculino;

b) Quantidade de pessoas de gênero  **f**eminino abaixo e acima de 18 anos

c) Quantidade de pessoas de gênero  **m**asculino abaixo e acima de 18 anos

Observaçãos: **use as letras f/m** na condição da estrutura de decisão
"""

fem = 0
masc = 0
fem_maior = 0
fem_menor = 0
masc_maior = 0
masc_menor = 0

cadastro = input('Deseja cadastrar (s/n)?')
while cadastro == 's':
    genero = input('Digite seu genero (f) para feminino e (m) para masculino: ')
    idade = int(input("Digite sua idade: "))

    if genero == 'f' or genero == 'F':
        fem = fem + 1
        if idade >= 18:
            fem_maior = fem_maior + 1
        else:
            fem_menor = fem_menor + 1

    if genero == 'm' or genero == 'M':
        masc = masc + 1
        if idade >= 18:
            masc_maior = masc_maior + 1
        else:
            masc_menor = masc_menor + 1
    cadastro = input('Deseja cadastrar outro (s/n)?')
print("Mulheres:", fem, "Homens:", masc)
print("Mulheres abaixo de 18:", fem_menor)
print("Mulheres acima de 18:", fem_maior)
print("Homens acima de 18:", masc_maior)
print("Homens abaixo de 18:", masc_menor)

# Digite seu código aqui
# item a) criar 2 contadores( f ou m )
# item b) criar 2 contadores( f )
# item b) criar 2 contadores( m )
while resposta == 's':