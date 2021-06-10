
n1 = int(input())
n2 = int(input())
primos = 0

for num in range(n1+1,n2+1):
    if all(num % i !=0 for i in range(2,num)):
        primos +=1
        print (num)
print (f'primos: {primos}')     

#correção aula:
def primo(n):
    qtd_divisores = 0
    for divisor in range (1,n+1):
        if n % divisor ==0:
            qtd_divisores+=1
    return qtd_divisores == 2        

inicio = int(input())
fim = int(input())
qtd_primos = 0

for n in range (inicio,fim +1):
    if primo (n):
        print(n)
        qtd_primos +=1
print(f'primos: {qtd_primos}')        


###