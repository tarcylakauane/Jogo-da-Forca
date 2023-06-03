from defs.categorias import categorias


def inicio():
    print(''' Feito por:
              Tárcyla Kauane dos Santos - 2023111790015@iesp.edu.br
              Com ajuda de:
              Wuldson Franco Fernandes da Silva - prof2214@iesp.edu.br
              Gabriel de Lisboa Medeiros - gabriel.medeiros@iesp.edu.br                                                     
              Diego Moura Araújo - 2022211510093@iesp.edu.br

              ''')
    print('-' * 70)
    print('JOGO DA FORCA'.center(70))
    print('-' * 70)
    print('''Categorias:
                [1] Frutas                                           
                [2] Cores                                           
                [3] Sair''')
    print('-' * 70)


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            categorias.limpar()
            print('\u001b[31mErro: Digite uma opção válida.\u001b[m')
            inicio()
            continue
        else:
            return n