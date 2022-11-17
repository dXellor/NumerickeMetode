import numpy as np

# Povratne vrednosti su matrice koje cine postavku testa i da li se trazi minimum(1) ili maksimum(0)
def test(broj_testa):
    A = np.array([
        [-3.0, 2.0],
        [2.0, -4.0],
        [1.0, 1.0],
        [-2.0, 1.0],
    ])

    b = np.array([
        [2.0, 3.0, 6.0, 0.0]
    ])

    extr = 0

    if broj_testa == 2:
        A = np.array([
            [1.0, 1.0],
            [1.0, -1.0],
            [2.0, -3.0],
        ])

        b = np.array([
            [4.0, 6.0, 0.0]
        ])

        extr = 1

    elif broj_testa == 3:
        A = np.array([
            [8.0, 6.0, 1.0],
            [4.0, 2.0, 1.5],
            [2.0, 1.5, 0.5],
            [0.0, 0.0, 1.0],
            [-60.0, -30.0, -20.0]
        ])

        b = np.array([
            [48.0, 20.0, 8.0, 5.0, 0.0]
        ])

        extr = 0

    elif broj_testa == 4:
        A = np.array([
            [60e3, 15e3],
            [60e3, 0.0],
            [-15e6, -3e6],
        ])

        b = np.array([
            [600e3, 540e3, 0.0]
        ])

        extr = 0

    elif broj_testa == 5:
        A = np.array([
            [1.0, 1.0],
            [2.0, 1.0],
            [-40.0, -30.0],
        ])

        b = np.array([
            [12.0, 16.0, 0.0]
        ])

        extr = 0

    elif broj_testa == 6:
        A = np.array([
            [2.0, 1.0],
            [2.0, 3.0],
            [3.0, 1.0],
            [-3.0, -2.0],
        ])

        b = np.array([
            [18.0, 42.0, 24.0, 0.0]
        ])

        extr = 0

    if broj_testa < 1 or broj_testa > 6:
        print("Niste izabrali validnu vrednost -> Izabran je test broj 1")

    return A, b, extr