import numpy as np
from simplex import simplex_method
from test_matrice_simplex import test

def main():
    choice = int(input("Unesite koji test zelite (1-6): "))
    A, b, extr = test(choice)

    x, x_sl, R = simplex_method(A, b, extr)
    print("\n<TABELA KRAJ>:\n", np.round(R,3))
    print("\nPROMENLJIVE:")
    for i in range(x.shape[0]):
        print(f'x{x[i]} = {R[i,0]}')
    
    print("\nSLOBODNE PROMENLJIVE:")
    for i in range(x_sl.shape[0]):
        if i == 0:
            continue
        print(f'x{x_sl[i]} = 0')

if __name__ == '__main__':
    main()