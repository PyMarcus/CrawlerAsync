from bs4 import BeautifulSoup
from colorama import Fore


class ParserRequestController:
    @staticmethod
    def parser(resposta):
        bs = BeautifulSoup(resposta, 'html.parser')
        titulo = bs.find('h2', {"class": "v_title"}).get_text()
        versiculos = bs.find_all('p')
        print(Fore.RED + titulo)
        contador = 0
        set_repeticao = []
        for linhas in versiculos:
            if linhas.text not in set_repeticao:
                set_repeticao.append(linhas.text)
            if " Salmo" in linhas.text:
                contador += 1
            if contador >= 2:
                break
        return set_repeticao