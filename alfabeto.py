
qtd = int(input())
alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for i in range(qtd):
    print(alfabeto[i]*(i+1))

#correção aula:
n = int (input())
letra = 'A'

for linha in range (1, n+1):
    print(letra * linha)
    letra = chr(ord(letra)+1)