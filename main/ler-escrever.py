import shutil


def escrever_arq(texto):
    arquivo = open('/home/samuel/teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()


def atualizar_arq(nome_arq, texto):
    arquivo = open(nome_arq, 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arq(nome_arq):
    arquivo = open(nome_arq, 'r')
    texto = arquivo.read()
    print(texto)


def media_notas(nome_arq):
    arq = open(nome_arq, 'r')
    aluno_nota = arq.read()
    aluno_nota = aluno_nota.split('\n')
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        def media(notas): return sum([int(i) for i in notas])/4
        print(media(lista_notas))
        lista_media.append({aluno: media(lista_notas)})
    return lista_media


def copia_arq(nome_arquivo):
    shutil.copy(nome_arquivo, '/home/samuel/')


def move_arq(nome_arq):
    shutil.move(nome_arq, '/home/samuel/')


if __name__ == '__main__':
    # lista_media = media_notas('notas.txt')
    # print(lista_media)
    # copia_arq('notas.txt')
    move_arq('notas.txt')
    # aluno = 'Ana, 10, 5, 5, 0\n'
    # atualizar_arq('notas.txt', aluno)
    # escrever_arq('samuel.')
