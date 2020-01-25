"""Jokenpo.

Jokenpo é uma brincadeira japonesa, onde dois jogadores escolhem um dentre 
três possíveis itens: Pedra, Papel ou Tesoura. O objetivo é fazer um juiz de 
Jokenpo que dada a jogada dos dois jogadores informa o resultado da partida.

As regras são as seguintes:
 - Pedra empata com Pedra e ganha de Tesoura
 - Tesoura empata com Tesoura e ganha de Papel
 - Papel empata com Papel e ganha de Pedra
"""


def jokenpo(entrada1, entrada2):
    """
    >>> jokenpo('pedra','pedra')
    (0, 'empate')

    >>> jokenpo('tesoura', 'tesoura')
    (0, 'empate')

    >>> jokenpo('papel', 'papel')
    (0, 'empate')

    >>> jokenpo('tesoura', 'pedra')
    (2, 'pedra')

    >>> jokenpo('pedra', 'tesoura')
    (1, 'pedra')

    >>> jokenpo('pedra', 'papel')
    (2, 'papel')

    >>> jokenpo('papel', 'pedra')
    (1, 'papel')

    >>> jokenpo('tesoura', 'papel')
    (1, 'tesoura')

    >>> jokenpo('papel', 'tesoura')
    (2, 'tesoura')
    """
    d = {
        'tesoura': 'papel',
        'pedra': 'tesoura',
        'papel': 'pedra'
    }

    if d[entrada1] == entrada2:
        return (1, entrada1)
    if d[entrada2] == entrada1:
        return (2, entrada2)

    return (0, 'empate')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
