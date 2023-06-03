from time import sleep
from defs.categorias import categorias
from defs.interface import interface

opcao = 0
while opcao != 3:
    interface.inicio()
    opcao = interface.leiaint('Digite uma opção: ')
    if opcao == 1:
        categorias.fruta()
    elif opcao == 2:
        categorias.cor()
    elif opcao == 3:
        categorias.limpar()
        print('Encerrando jogo...')
        sleep(2)
    else:
        categorias.limpar()
        print('Opção inválida. Tente novamente!')
print('Jogo encerrado.')