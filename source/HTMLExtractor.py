import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from source.Utilitaire import *
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
        tablesSelected = pageHTML.select('table[class="wikitable"]')

        for table in pageHTML.select('table.wikitable'):
            fileName = url + " - " + str(tableNumber) + ".csv"
            with open(fileName, 'w', newline='', encoding="utf-8") as file:
                writer = csv.writer(file, delimiter=';')
                tableNumber = tableNumber + 1


                isCreated = False
                nbrOfRows = len(list(table.select('tr')))
                nbrOfColumns = len(table.select('tr')[0].select('th'))

                newTable = []

                for row in table.select('tr'):
                    columns = row.findChildren(recursive=False)
                    tempLine = []
                    for column in columns:
                        tempLine.append(column.text.strip())
                    newTable.append(tempLine)
                writer.writerows(newTable)

                """for row in table.select('tr'):
                    currentRow = list()

                    for column in row.select('th'):
                        currentRow.append(column.text.strip())
                        print(column.text.strip())

                    for column in row.select('td'):
                        currentRow.append(column.text.strip())
                        print(column.text.strip())

                    print(currentRow)
                    newTable.append(currentRow)
                writer.writerows(currentRow)



for ligne in lignes:
    columns = ligne.findChildren(recursive = False)
    output_row = []
    for column in columns:
        output_row.append(column.text.strip())
    output_rows.append(output_row)
writer.writerows(output_rows)

"""












"""
class WikipediaHTMLExtractor {

CSVEditor csvEditor = new CSVEditor();

public void extractor(String URL ) throws IOException {

// Récupération du HTML à partir de l'URL
String BASE_WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/";
String wurl = BASE_WIKIPEDIA_URL + URL;


try {

Document doc = Jsoup.connect(wurl).get();

// Récupération des tables dans le DOM
Elements table = doc.getElementById("mw-content-text") // Filtres
.select("table:not(.metadata)")
.select("table:not([class*=navbox])") // toutes les classes qui contiennent la valeur "navbox"
.select(".wikitable")
.select("table:not([class*=collapse])");

// boucle sur tous les tableaux sélectionné
for (int i = 0; i < table.size(); i++) {

int nbrColonne = 0;

Element currentTable = table.get(i);
Elements rows = currentTable.select("tr");

String docPath = "./output/html/" + URL + "-" + (i+1) +".csv";

// je crée un tableau dont le nombre de ligne est égale au nombre de ligne de mon tableau HTML et représente le futur CSV
// On ajoutera les lignes du CSV au fur et à mesure du traitement
ArrayList < ArrayList < String >> dataTest = new ArrayList < ArrayList < String >> ();

// ATTENTION s'il y a du rowspan = n ~> colone imbriquée; il faut récupérer le rowspan et faire n ajout
//[attr] elements with an attribute named "attr" (with any value)

// boucle sur toutes les lignes du tableau i
for (int j = 0; j < rows.size(); j++) {
Element row = rows.get(j);
ArrayList < String > tempLine = new ArrayList < String > ();

Elements headers = row.select("th");
Elements cols = row.select("td");

// Ici je vérifie s'il y a des headers tout en m'assurant de ne pas prendre de ligne complète
if ((headers.size() != 0) & !(nbrColonne == headers.size())) {
for (int k = 0; k < headers.size(); k++) {

nbrColonne = headers.size();
Element col = headers.get(k);

String nbrRowspan = col.attr("colspan");
int colspanToInt = Integer.parseInt("0" + nbrRowspan);
if (colspanToInt > 0) {
for (int m = 0; m < colspanToInt; m++) {
tempLine.add(col.text());
}
}
tempLine.add(col.text());
}
}

// boucle sur tous les colonnes de la ligne j du tableau i
for (int k = 0; k < cols.size(); k++) {
Element col = cols.get(k);
// On ajoute l'élément à notre ligne
tempLine.add(col.text());
}
// On ajoute la ligne au CSV
dataTest.add(tempLine);
}
// On crée le CSV du tableau
csvEditor.createCSVFile(docPath, dataTest);
}

}
catch(Exception
e) {
    System.out.println("Erreur lors de l'extraction de la page " + wurl);
System.out.println(e);
}

}

}
"""


