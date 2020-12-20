from input.wikiurls import wikiurls
from source.HTMLExtractor import HTMLExtractor

extractor = HTMLExtractor()

if __name__ == '__main__':

    nbrPageTraitee = 0

    for i in range(0,len(wikiurls)):
        url = wikiurls[i]
        extractor = HTMLExtractor()
        extractor.extractor(url)
        nbrPageTraitee = nbrPageTraitee + 1



