l1 = int(input('Digite o valor do primeiro lado: '))
l2 = int(input('Digite o valor do segundo lado: '))
l3 = int(input('Digite o valor do terceiro lado: '))

if(l1<=0) or (l2<=0) or (l3<=0):
    print('O valor de um dos lados é inválido')
else:
    if(l2+l3<=l1) or (l1+l3<=l2) or (l1+l2<=l3):
        print('Os lados não formam um triângulo')
    elif(l1==l2==l3):
        print('Triângulo equilátero')
    elif(l1!=l2) and (l1!=l3) and (l2!=l3):
        print("Triângulo escaleno")
    else:
        print('Trinângulo isósceles')