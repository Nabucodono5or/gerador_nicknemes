import gerar_nicks


def start():
    opcao = -1
    while True:
        print("Gerador automático de nicks para games ou profiles!!")
        opcao = input("escolha uma opção:")
        menu_opcao()

    nick = gerar_nicks.gerar_nicks()
    print(nick)



def gerar_nick():
    gerar_nicks.gerar_nicks()

def sair():
    break

def menu_opcao(opcao):
    switcher = {
        0: sair
        1: gerar_nick,
    }
    switcher.get(opcao, lambda: "Invalid option")

