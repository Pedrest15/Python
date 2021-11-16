import pandas as pd
from time import sleep

def maiores_notas(lista_animes):
    str = input("Gostaria de ver os 5 animes com maiores notas? => ")
    print("\n")
    str = str.strip().capitalize().lower().replace('ã', 'a')
    while 1:
        if str == 'sim':
            print(lista_animes.head())
            print('\n')
            break
        elif str == 'nao':
            print("\n")
            break
        else:
            print("Por favor, responda com 'sim' ou 'não'\n")

def animes_famosos_ocidente(lista_animes):
    str = input("Gostaria de ver as notas de 6 dos animes mais famosos no ocidente? => ")
    print("\n")
    str = str.strip().capitalize().lower().replace('ã', 'a')
    while 1:
        if str == 'sim':
            animes_ocidente = lista_animes.query("name == 'Dragon Ball'")
        
            nomes_ocidente = ['Dragon Ball Z', 'Dragon Ball GT', 'Naruto', 'Saint Seiya', 'Fullmetal Alchemist: Brotherhood']
            for i in nomes_ocidente:
                aux = lista_animes.query("name == '{}'".format(i))
                animes_ocidente = pd.merge(animes_ocidente, aux, how='outer')
            print(animes_ocidente)
            print("\n")
            break
        elif str == 'nao':
            print("\n")
            break
        else:
            print("Por favor, responda com 'sim' ou 'não'\n")

def busca_animes(lista_animes):
    flag = 0
    while 1:
        str = input("Deseja procurar algum anime? Responda com 'sim' ou 'não' => ")
        str = str.strip().capitalize().lower().replace('ã', 'a')
        if str == 'nao':
            return -1
        if str != 'nao' and str != 'sim':
            continue

        nome_anime = input("\nDigite o nome do anime que deseja buscar => ")
        j = 0
        for i in lista_animes.name:
            if i.strip().capitalize().lower() == nome_anime.strip().capitalize().lower():
                print(lista_animes.loc[j])
                print("\n")
                if flag == 0:
                    aux = lista_animes.query("index == {}".format(j))
                    animes_buscados = aux
                    flag = 1
                elif flag == 1:
                    aux = lista_animes.query("index == {}".format(j))
                    animes_buscados = pd.merge(animes_buscados, aux, how='outer')
                break
            else:
                print("Desculpe, anime não encontrado.\n")  
            j += 1  
    return animes_buscados  

def tabela_busca(animes_buscados):
    str = input("\nDeseja baixar uma tabela com os animes buscados por você? ") 
    str = str.strip().capitalize().lower().replace('ã', 'a') 
    if animes_buscados == -1:
        print("Desculpe, mas você não buscou nenhum anime.\n")
        return
    while 1:
        if str == 'sim':
            animes_buscados.to_csv('animes-buscados.csv', sep = ',')
            print("...")
            sleep(2)
            print('Pronto! Download realizado com sucesso\n')
            break
        elif str == 'nao':
            break
        else:
            print("Por favor, responda com 'sim' ou 'não'\n")

if __name__ == '__main__':
    lista_animes = pd.read_csv('anime.csv')

    maiores_notas(lista_animes)
    animes_famosos_ocidente(lista_animes)
    animes_buscados = busca_animes(lista_animes)
    tabela_busca(animes_buscados)
