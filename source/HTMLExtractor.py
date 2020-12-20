import os

import requests
from bs4 import BeautifulSoup
import csv


class HTMLExtractor():

    def extractor(self, url):
        """Extrait les tableaux d'une page à partir d'un URL donnée

        :param url: String, url de la page web dont on veut extraire les tableaux
        :return: void
        """

        # Récupération et mise en forme de l'URL
        baseWikiURL = "https://en.wikipedia.org/wiki/"
        wurl = baseWikiURL + url

        tableNumber = 1

        pageWeb = requests.get(wurl)
        pageHTML = BeautifulSoup(pageWeb.content, 'html.parser')

        for table in pageHTML.select('table.wikitable'):
            fileName = os.getcwd() + "/output/" + url + " - " + str(tableNumber) + ".csv"
            with open(fileName, 'w', newline='', encoding="utf-8") as file:
                writer = csv.writer(file, delimiter=';')
                tableNumber = tableNumber + 1

                newTable = []

                for row in table.select('tr'):
                    columns = row.findChildren(recursive=False)
                    tempLine = []
                    for column in columns:
                        tempLine.append(column.text.strip())
                    newTable.append(tempLine)
                writer.writerows(newTable)

