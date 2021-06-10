divida = int(input())
pagar = int(input())
pagamento = 0

while divida > 0:
    pagamento += 1
    print(f'pagamento: {pagamento}')
    print(f'antes = {divida}')

    if divida < pagar:
        divida = 0
        print(f'depois = {divida}')
        print('-' * 5)
    else:
        divida = divida - pagar  
        print(f'depois = {divida}')
        print('-' * 5)


#correção aula:

valor_divida = int(input())
valor_mensal = int(input())
pagamento = 0

while valor_divida > 0:
    pagamento += 1
    print(f'pagamento: {pagamento}')
    print(f'antes = {valor_divida}')
    if valor_mensal < valor_divida:
        valor_divida -= valor_mensal
    else:
        valor_divida = 0 
    print(f'depois = {valor_divida}')   
    print('-' * 5)   