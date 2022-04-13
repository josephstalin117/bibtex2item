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

def check_type(r):
    entry_type = re.search(r'@(.*?){.*?', r).group(1)
    return entry_type


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
        m = re.search(key + r'={(.*?)}',content)
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

def parse_conferencename(conference_name):
    #print(conference_name)
    m = re.search(r'Proceedings',conference_name)
    if m:
        new_conference_name = re.sub('Proceedings', 'Proc.', conference_name)
    else:
        new_conference_name = "Proc. of the " + conference_name
    # IJCAI
    new_conference_name = re.sub('IJCAI', 'of the International Joint Conferences on Artificial Intelligence (IJCAI)', new_conference_name)
    return new_conference_name


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
    conference["booktitle"] = parse_conferencename(conference["booktitle"])

    return conference


def bibtex2bibitem_conference(bibtex):

    bibitem = ""

    bibitem = bibtex["author"] + ', ``{}", '.format(bibtex["title"])
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
    bibitem = ""

    bibitem = bibtex["author"] + ', ``{}",'.format(bibtex["title"])
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


def bibtex2bibitem(bibtex):
    bibitems = []
    bibitem = ""
    for r in bibtex:
        entry_type = check_type(r)
        if entry_type == "article":
            article = parse_article(r)
            bibitem = bibtex2bibitem_article(article)
            bibitems.append(bibitem)
        else:
            conference = parse_conference(r)
            bibitem = bibtex2bibitem_conference(conference)
            bibitems.append(bibitem)
        bibitem = ""

    return bibitems


if __name__ == '__main__':
    bibs = parse_bibs("./test.bib")
    #article = parse_article(bibs[-1])
    #bibitem = bibtex2bibitem_article(article)
    #print(bibitem)

    #conference = parse_conference(bibs[3])
    #bibitem = bibtex2bibitem_conference(conference)
    #print(bibitem)
    bibitems = bibtex2bibitem(bibs)
    for bibitem in bibitems:
        print(bibitem)