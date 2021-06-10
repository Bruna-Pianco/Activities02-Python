total= 0
real =0

valor_vic = float(input())

while valor_vic != -1:

    total += valor_vic
    valor_vic = float(input())

conversao_vic = (total * 2.50)  

print(f'VC$ {total:.2f}') 
print(f'R$ {conversao_vic:.2f}')

#correção

total_vic = 0
vic_coin = float(input())

while vic_coin != -1.0:
    total_vic+=vic_coin
    vic_coin = float(input())

total_reais = total_vic * 2.50
print(f'VC$ {total_vic:.2f}') 
print(f'R$ {total_reais:.2f}')
