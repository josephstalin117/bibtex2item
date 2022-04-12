import sys
import re

def parse_bibs(filename):
    with open(filename, 'r') as f:
        r = f.readlines()
    bib = ""
    bib_list = []
    # print(bibtex)
    # r = bibtex.split('\n')
    i = 0
    while i < len(r):
        line = r[i].strip()

        if not line:
            i += 1
        elif '@' == line[0]:
            bib = ""
            bib = line
            i += 1
        elif '}' == line[0]:
            bib += line
            bib_list.append(bib)
            bib = ""
            i += 1
        else:
            bib += line
            i += 1

    return bib_list

def parse_article(r):
    article = {"entry_type":"",
               "cation_key":"",
                "title":"",
                "author":"",
                "journal":"",
                "volume":"",
                "number":"",
                "pages":"",
                "year":"",
                "publisher":"",
               }
    article["entry_type"] = re.search(r'@(.*?){.*?', r).group(1)
    search_result = re.search(r'(.*?),(.*?$)', r)
    article["cation_key"] = re.search(r'{(.*?)$', search_result.group(1)).group(1)
    content = search_result.group(2)
    for key, value in article.items():
        m = re.search(key + r'={(.*?)},',content)
        if m:
            article[key] = m.group(1)
    
    article["author"] = parse_authors(article["author"])

    return article


def parse_authors(authors):
    authors_list = []
    output_authors = ""
    for LastFirst in authors.split('and'):
        lf = LastFirst.replace(' ', '').split(',')
        if len(lf) != 2: continue
        last, first = lf[0], lf[1]
        authors_list.append("{}. {}".format(first.capitalize()[0], last.capitalize()))
    if len(authors_list) == 1:
        output_authors = authors_list[0]
    else:
        output_authors = ", ".join(_ for _ in authors_list[:-1]) + " and " + authors_list[-1]
    return output_authors


def parse_conference(r):
    conference = {"entry_type":"",
                "cation_key":"",
                "title":"",
                "booktitle":"",
                "journal":"",
                "author":"",
                "volume":"",
                "number":"",
                "pages":"",
                "year":"",
                "publisher":"",
               }
    conference["entry_type"] = re.search(r'@(.*?){.*?', r).group(1)
    search_result = re.search(r'(.*?),(.*?$)', r)
    conference["cation_key"] = re.search(r'{(.*?)$', search_result.group(1)).group(1)
    content = search_result.group(2)
    for key, value in conference.items():
        m = re.search(key + r'={(.*?)}',content)
        if m:
            conference[key] = m.group(1)

    
    conference["author"] = parse_authors(conference["author"])

    return conference


def bibtex2bibitem_conference(bibtex):
    bibitems = []
    bibitem = ""

    bibitem = bibtex["author"] + ', ``{}". '.format(bibtex["title"])
    print(bibitem)
    if bibtex["booktitle"]:
        bibitem = bibitem + 'in \emph{' + bibtex["booktitle"] + '}, '
    if bibtex["journal"]:
        bibitem = bibitem + 'in \emph{' + bibtex["journal"] + '}, '
    if bibtex['volume']:
        bibitem = bibitem + 'vol. ' + bibtex["volume"] + ', '
    if bibtex["number"]:
        bibitem = bibitem + 'no. ' + bibtex["number"] + ', '
    if bibtex["pages"]:
        bibitem = bibitem + 'pp. ' + bibtex["pages"] + ', '
    if bibtex["year"]:
        bibitem = bibitem + bibtex["year"]
    return bibitem

def bibtex2bibitem_article(bibtex):
    bibitems = []
    bibitem = ""

    bibitem = bibtex["author"] + ', ``{}". '.format(bibtex["title"])
    print(bibitem)
    if bibtex["journal"]:
        bibitem = bibitem + ' \emph{' + bibtex["journal"] + '}, '
    if bibtex['volume']:
        bibitem = bibitem + 'vol. ' + bibtex["volume"] + ', '
    if bibtex["number"]:
        bibitem = bibitem + 'no. ' + bibtex["number"] + ', '
    if bibtex["pages"]:
        bibitem = bibitem + 'pp. ' + bibtex["pages"] + ', '
    if bibtex["year"]:
        bibitem = bibitem + bibtex["year"]
    return bibitem


if __name__ == '__main__':
    bibs = parse_bibs("./gatattn.bib")
    #print(bibs)
    article = parse_article(bibs[0])
    print(article)
    bibitem = bibtex2bibitem_article(article)
    print(bibitem)

    print(bibs)
    conference = parse_conference(bibs[4])
    print(conference)
    bibitem = bibtex2bibitem_conference(conference)
    print(bibitem)
    