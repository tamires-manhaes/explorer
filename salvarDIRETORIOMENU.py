# -*- coding:utf-8 -*-

import os
import os.path
import shutil
import glob

caminhoPAI = '/Users/proce/Desktop/explorer2/'


def title(tl):
    print('=' * 80)
    print(f'{tl:^80}'.upper())
    print('=' * 80)
    print()


def acess_dir(caminho):
    with os.scandir(caminho) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_dir():
                print('\t', entry.name)


def ver_dir(diretorio):
    if not os.path.exists(diretorio):
        os.mkdir(diretorio)  # Se não existir, cria diretório
        print('Diretório criado com sucesso!')
    else:
        print('Diretório já existe!')


def listar_arquivos(caminho):
    with os.scandir(caminho) as it:
        for entrar in it:
            if not entrar.name.startswith('.') and entrar.is_file():
                print('\t', entrar.name)


def listar_dir():
    for filename in glob.iglob(caminhoPAI, recursive=True):
        print('_' * 80)
        print('Pasta acessada: ', end='')
        print(filename)


def menu_diretorios():
    title('Navegando pelo Menu DIRETÓRIOS')
    print('Escolha sua opção: ')
    op = str(input('''
        [mkdir] - Criar diretórios
        [rm] - Apagar diretórios
        [cd] - Acessar diretórios
        [ls] - Listar Arquivos
        [exit] - Retornar/Sair
        Opção: ''')).lower()

    if op == 'exit':
        exit(1)
# ------------------------------------------------------------------------------------------- #
    elif op == 'mkdir':  # CRIAR DIRETORIOS
        j = 'S'
        while j == 'S':
            print('Para criar subpastas utilize "/" ')
            ver_dir(str(input('Nome do diretório: ')))
            j = str(input('Deseja criar um novo diretório? [S/N]')).upper()
        menu_diretorios()
# ------------------------------------------------------------------------------------------- #
    elif op == 'rm':  # APAGAR DIRETORIOS
        listar_dir()
        tem = (str(input('Informe o nome da pasta a ser apagada: ')))
        dir_del = tem
        if not os.path.exists(dir_del):
            j = 'S'
            while j == 'S':
                j = str(input('Pasta inexistente. Deseja tentar outra? [S/N]')).upper()
        else:
            for caminho, pastas, arquivos in os.walk(caminhoPAI):
                for pasta in pastas[:]:
                    if pasta == dir_del:
                        pastas.remove(pasta)
                        shutil.rmtree(os.path.join(caminho, pasta))
                        print('Pasta removida!')
        menu_diretorios()
# ------------------------------------------------------------------------------------------- #
    elif op == 'cd':  # ACESSAR DIRETORIOS
        # print('_' * 40)
        listar_dir()
        acess_dir(caminhoPAI)
        tem = (str(input('Informe o nome da pasta a ser acessada: ')))
        dir_acesso = tem
        if not os.path.exists(dir_acesso):
            j = 'S'
            while j == 'S':
                j = str(input('Pasta inexistente. Deseja tentar outra? [S/N]')).upper()
        else:
            caminho_atual = caminhoPAI + tem
            for caminho, pastas, arquivos in os.walk(caminho_atual):
                for pasta in pastas:
                    print(os.path.join(caminho, pasta))
                    os.chdir(caminho)
                    listar_dir()

                    # if pasta == dir_acesso:
                    #    caminho = tem
                    #    os.chdir(caminho)
                    #    print('Pasta acessada!')
                    #    listar_dir()
        print('_' * 80)

        menu_diretorios()
# ------------------------------------------------------------------------------------------- #
    elif op == 'ls':  # LISTAR ARQUIVOS
        listar_dir()
        caminho = caminhoPAI
        print(listar_arquivos(caminho))
        # print(os.getcwd())
        menu_diretorios()

# ------------------------------------------------------------------------------------------- #
    else:
        print("Esta opção não está nas alternativas, tente novamente.\n")
        menu_diretorios()


print(menu_diretorios())
