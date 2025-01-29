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

from tkinter import Tk,Label,Entry,Button
from tkinter.messagebox import showinfo

def calcular(ent, ent_1):
    term,term_1 = (int(ent_i.get()) for ent_i in (ent,ent_1))

    _1ªdescon,_2ªdescon = map(descompon, (term, term_1))
    cadena = ' + '.join(f'{elem} * {elem_1}' for elem in _1ªdescon for elem_1 in _2ªdescon)
    res = sum(elem * elem_1 for elem in _1ªdescon for elem_1 in _2ªdescon)
    tupla = (f'{term} * {term_1}',
          f"{' * '.join(map(a_Suma, (_1ªdescon, _2ªdescon)))}",
          f"{' + '.join(f'{elem} * {a_Suma(_2ªdescon)}' for elem in _1ªdescon)}",
          f'{cadena} = {res}',
          f'True debe ser {res == term * term_1}')

    showinfo("Resultado",'\n'.join([' = '.join(tupla[:-1]), tupla[-1]]))
    
def config(nº):
    Label(root, text=f"Número {nº}:").pack()
    ent = Entry(root)
    ent.pack()

    return ent

root = Tk()
root.title("Multiplicador")

entry,entry1=(config(nº) for nº in (1,2))

Button(root, text="Calcular", command=lambda: calcular(entry, entry1)).pack()
root.mainloop()

'''
term, term_1 = tuple(int(input(f'Introduzca {pos} term: ')) for pos in ('1er', '2º'))
_1ªdescon,_2ªdescon = map(descompon, (term, term_1))
cadena = ' + '.join(f'{elem} * {elem_1}' for elem in _1ªdescon for elem_1 in _2ªdescon)
res = sum(elem * elem_1 for elem in _1ªdescon for elem_1 in _2ªdescon)
tupla = (f'{term} * {term_1}',
      f"{' * '.join(map(a_Suma, (_1ªdescon, _2ªdescon)))}",
      f"{' + '.join(f'{elem} * {a_Suma(_2ªdescon)}' for elem in _1ªdescon)}",
      f'{cadena} = {res}',
      f'True debe ser {res == term * term_1}')

print(' = '.join(tupla[:-1]),'\n',tupla[-1])
'''
