def descompon(num):
    #OBJ: nº -> términos de 10 ^ exp
    #PRE: int
    cifras, lista = len(str(num)), []
    potencia = 10 ** (cifras - 1)#> potia inicial, 1e1
    
    while potencia > 0:
        factor = num // potencia * potencia
        
        if factor > 0: lista.append(factor) 

        num %= potencia
        potencia //= 10
    
    return tuple(lista) 

def a_Suma(tupla):
    return f"({' + '.join(map(str, tupla))})"

#PROGRAMA
_1ªdescon,_2ªdescon = map(descompon, (1234, 5678))
cadena = ' + '.join(f'{elem} * {elem_1}' for elem in _1ªdescon for elem_1 in _2ªdescon)
res = sum(elem * elem_1 for elem in _1ªdescon for elem_1 in _2ªdescon)
tupla = ('1234 * 5678',
      f"{' * '.join(map(a_Suma, (_1ªdescon, _2ªdescon)))}",
      f"{' + '.join(f'{elem} * {a_Suma(_2ªdescon)}' for elem in _1ªdescon)}",
      f'{cadena} = {res}',
      f'True debe ser {res == 1234 * 5678}')

print(' = '.join(tupla[:-1]),'\n',tupla[-1])
