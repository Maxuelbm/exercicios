a1 = int(input('Digite o valor do primeiro ângulo: '))
a2 = int(input('Digite o valor do segundo ângulo: '))
a3 = int(input('Digite o valor do terceiro ângulo: '))

if(a1<=0) or (a2<=0) or (a3<=0):
    print('Valores inválidos')
elif (a1+a2+a3!=180):
    print('Os valores não formam um triângulo')
elif (a1<90) and (a2<90) and (a3<90):
    print('Triângulo Acutângulo')
elif (a1==90) or (a2==90) or (a3==90):
    print('Triãngulo retângulo')
else:
    print('Triãngulo obtusangulo')
