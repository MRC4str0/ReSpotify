from SpotReq import SpotReq
from termcolor import colored as color
from time import sleep
from Secrets import cred

print('''
  _____       _____             _   _  __
 |  __ \     / ____|           | | (_)/ _|
 | |__) |___| (___  _ __   ___ | |_ _| |_ _   _
 |  _  // _ \___ \| '_ \ / _ \| __| |  _| | | |
 | | \ \  __/____) | |_) | (_) | |_| | | | |_| |
 |_|  \_\___|_____/| .__/ \___/ \__|_|_|  \__, |
                   | |                     __/ |
                   |_|                    |___/

''')
print('/' * 100)

while True:

    try:
        playlist_url = str(input('Playlist Url: '))
        spot = SpotReq(cred['client_id'], cred['client_secret'])
        dados = spot._getDados(playlist_url)

    except:
        print(color('URL NÃO SUPORTADA!', 'red'))
        print('\n' + '.' * 100)

    else:
        break


print('\n' + ('.' * 100))
print(f'''Playlist: {dados["nome"]}          Tracks: {dados["tracks"]}          Publico: {dados["public"]}
Descrição: {dados["descri"]}\n''')

start = str(input('Continuar? (S / N): ')).strip().upper()[0]

if start == 'S':
    print('\n' + '.' * 100)
    for l in 'DEPOIS DE CONCLUIDO, O PROCESSO NÃO PODERA SER REVERTIDO!':
        print(color(f'{l}', 'red'), end = '', flush = True)
        sleep(0.03)
    sleep(3)

    print('''\n
    [1] Ascendente (C/Artista)
    [2] Descendente (C/Artista)
    [3] Aleatório''')

    while True:
        try:
            opc = int(input('\nOpção: '))
        except:
            print('Opção Invalida!')
        else:
            if opc not in (1, 2, 3):
                print('Opção Invalida!')
            else:
                break
        sleep(1)


    print('\n' + '.' * 100)
    for l in 'RECOMEDAMOS NÃO INTERFERIR NA PLAYLIST DURANTE O PROCESSO!':
        print(color(f'{l}', 'red'), end = '', flush = True)
        sleep(0.03)
    print('\nAguarde...\n')

    try:
        plist_dict = spot.scanner(playlist_url)
        list_uri = spot.TipoPlaylist(opc, plist_dict)
        spot.add_playlist(list_uri, playlist_url)

    except Exception as Error:
        print(color('FALHA NA FINALIZAÇÃO DO PROCESSO', 'red'))
        print(f'Erro: {Error}')

    else:
        print(color('PROCESSO FINALIZADO COM SUCESSO!', 'green'))
        esc = input(f'Pressione {color("ENTER", "yellow")} para sair!')
