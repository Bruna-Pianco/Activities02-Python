inicio = int(input())
fim = int(input())
anos = 0

for i in range(inicio, fim +1):
    if (i % 4 == 0 and i % 100 !=0) or i % 400 == 0:
        anos +=1
        print(i)
print(f'bissextos: {anos}')
           

#correção aula:

def bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or ano % 400 ==0   

inicio = int(input())
fim = int(input())
qtd_bissextos = 0

for ano in range (inicio,fim +1):
    if bissexto (ano):
        print(ano)
        qtd_bissextos +=1

print (f'bissextos: {qtd_bissextos}')
