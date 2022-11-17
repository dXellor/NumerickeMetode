import numpy as np

# A - Matrica parametara koji stoje uz slobodne promenljive x 
# b - Matrica clanova sa desne strane jednakosti
# extr = 0 - trazimo maksimum, extr = 1 - trazimo minimum
# NAPOMENA1: Matrice A i b se odnose na parametre uz slobodne promenljive i u ogranicenjima I u kriterijumu optimalnosti,
# gde se kriterijum optimalnosti nalazi u zadjem redu
# NAPOMENA2: Kriterijum optimalnosti mora biti definisan kako je nalozeno kod Simplex metode

def check(T, extr):
    if extr == 0:
        return T >= 0
    else:
        return T <= 0

def simplex_method(A, b, extr=0):
    A = np.insert(A, 0, b, 1)                                           # Prosirujemo matricu A sa kolonom koja sadrzi slobodne clanove
    rows, cols = A.shape
    if extr == 0:
        uslov1, uslov2, extr_txt  = np.amin, np.argmin, 'maksimum'
    else:
        uslov1, uslov2, extr_txt = np.amax, np.argmax, 'minimum'
        
    x_sl = np.arange(0, cols)                                           # Slobodne promenljive
    x = np.arange(cols, cols+rows-1)                                

    print(f'\n<TABELA POCETAK (trazimo {extr_txt})>:\n', np.round(A,3))
    while True:
        T = uslov1(A[-1:])
        if check(T, extr):
            break                                                       

        cpyA = np.copy(A)                                               
        ec = uslov2(A[-1:])                                             # Indeks pivotske kolone
        with np.errstate(divide='ignore'):                              # Privremeno iskljucujemo upozorenje da delimo sa nulom jer to nije problem
            cpyA[:-1, 0] = np.divide(cpyA[:-1, 0], cpyA[:-1, ec])       # Delimo kolonu slobodnih clanova sa pivotskom kolonom (odgovarajuce elemente jedne sa drugima)
        er = np.where(cpyA[:-1, 0] > 0, cpyA[:-1, 0], np.Inf).argmin()  # Indeks pivotskog reda
        ep = A[er, ec]                                                  # Pivotski element

        x_sl[ec], x[er] = x[er], x_sl[ec]                               # Zamenimo slobodnu promenljivu iz ec kolone sa promenljivom iz er reda 
                                                                        # (ovo radimo kako bi ispratili koje promenljive uticu na optimizaciju) 
        newA = np.copy(A)

        # Prvo racunamo sve elemente nove tabele koji nisu u pivotskoj koloni i pivotskom redu
        Aec = A[:, ec]         
        Mec = np.broadcast_to(Aec[:, np.newaxis], (rows, cols))
        Aer = A[er, :]
        Mer = np.broadcast_to(Aer, (rows, cols))
        newA = A - (Mer*Mec)/ep

        # Racunamo elemente redom na pivotskoj koloni, pivotskom redu, i na kraju sam pivotski element
        newA[:, ec] = -1*Aec/ep
        newA[er, :] = Aer/ep
        newA[er, ec] = 1/ep

        A = newA

    return x, x_sl, A

        
