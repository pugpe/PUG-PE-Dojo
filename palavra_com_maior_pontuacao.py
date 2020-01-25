# while inotifywait -e close_write palavra_com_maior_pontuacao.py; do clear; python palavra_com_maior_pontuacao.py; done

# from string import ascii_lowercase

# d = {letter: i + 1 for i, letter in enumerate(ascii_lowercase)}


# def word_value(palavra):
#     """
#     >>> word_value('a')
#     1
#     >>> word_value('abc')
#     6
#     >>> word_value('z')
#     26
#     >>> word_value('ac')
#     4
#     """
#     return sum(d[letra] for letra in palavra)


def maior_pontuacao(frase):
    """
    >>> maior_pontuacao('inloco')
    'inloco'
    >>> maior_pontuacao('outrapalavra')
    'outrapalavra'
    >>> maior_pontuacao('a d')
    'd'
    >>> maior_pontuacao('a b')
    'b'
    >>> maior_pontuacao('ab ba')
    'ab'
    >>> maior_pontuacao('a b')
    'b'
    >>> maior_pontuacao('')
    ''
    """
    # Primeira solução *Incompleta*
    # resultado = ''

    # palavras = frase.split(" ")
    # palavras.reverse()

    # for p in palavras:
    #     pontuacao = word_value(p)
    #     dic[p] = pontuacao
    #     for i in dic:

    
    # Segunda solução
    if frase == '':
        return ''
    return max(frase.split(), key=lambda k: sum(ord(c) - 96 for c in k))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
