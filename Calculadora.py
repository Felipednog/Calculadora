def conversor_para_decimal(numero, base):
    if base == 'binario':
        return int(numero, 2)
    elif base == 'octal':
        return int(numero, 8)
    elif base == 'hexadecimal':
        return int(numero, 16)
    else:
        return int(numero)

def conversor_de_decimal(valor, base):
    if base == 'binario':
        return bin(valor)[2:]
    elif base == 'octal':
        return oct(valor)[2:]
    elif base == 'hexadecimal':
        return hex(valor)[2:]
    else:
        return str(valor)

def calcular(numero1, base1, numero2, base2, operacao):
    decimal1 = conversor_para_decimal(numero1,base1)
    decimal2 = conversor_para_decimal(numero2,base2)

    if operacao == 'soma':
        resultado_decimal = decimal1 + decimal2
    elif operacao == 'subtracao':
        resultado_decimal = decimal1 - decimal2
    elif operacao == 'multiplicacao':
        resultado_decimal = decimal1 * decimal2
    else:
        return 'Operação Inválida'

    return resultado_decimal

def calculadora ():
    numero1 = input("Qual o seu primeiro valor? :")
    base1 = input('Qual a base desse valor: binario, decimal, octal ou hexadecimal?: ')
    numero2 = input('Qual o seu segundo valor? : ')
    base2 = input('Qual a base desse valor: binario, decimal, octal ou hexadecimal?: ')
    operacao = input('Qual operação você deseja realizar: (soma, subtracao ou multiplicacao):')

    resultado_decimal = calcular(numero1, base1, numero2, base2, operacao)


    base_saida = input('Qual base final você deseja: binario, decimal, octal, hexadecimal?: ')
    resultado_final = conversor_de_decimal(resultado_decimal,base_saida)

    print(f'O resultado de {numero1}({base1}) {operacao} {numero2}({base2}) é igual a: {resultado_final}({base_saida})')


calculadora()




