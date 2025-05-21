num = int(input ("Somar números até: "))

"""
 Use as funcionalidades de debug do VSCode para corrigir o erro a seguir 
"""

soma = 0
x = 1
while x <= num:
    soma += x
x += 1

print ("A soma de 1 até",num, "é:", soma)