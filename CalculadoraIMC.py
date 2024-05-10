confirmar = int(input('Boas vindas ao calculador de IMC! Deseja continuar? (1 - sim, 0 - não): '))
if confirmar==0:
    exit()
elif confirmar==1:
    peso = int(input('Digite o seu peso (kg): '))
    altura = int(input('Digite a sua altura (cm): '))
    valor = peso/(altura**2)
    print('O seu valor IMC é de: ', valor)
else:
    print('Digitaste um número errado!')
    exit()