import lista_de_nicks
from random import randint

nicknames = lista_de_nicks.nicaknames


def gerar_nicks():
    index = randint(0, len(nicknames))
    return nicknames[index]
