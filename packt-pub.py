#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Client web per wwww.udl.cat/
@author: mov4
'''

import urllib2
from bs4 import BeautifulSoup

url = "https://www.packtpub.com/packt/offers/free-learning/"


class Client(object):
    """Obtenir Buscar Imprimir"""

    def get_web(self, page):
        f = urllib2.urlopen(page)
        html = f.read()
        f.close()
        return html

    def search_text(self, html):
        """Buscar en l'html"""
        soup = BeautifulSoup(html, 'html.parser')
        elements = soup.find_all("div", "dotd-title")
        titles = []
        for element in elements:
            title = element.text
            title = title.strip('\t\n')
            titles.append(title)
        return titles

    def print_resultat(self, resultats):
        if len(resultats) == 0:
            print "No title found"
        else:
            for resultat in resultats:
                print resultat

    def run(self):
        web = self.get_web(url)
        resultat = self.search_text(web)
        self.print_resultat(resultat)


if __name__ == "__main__":
    client = Client()
client.run()
