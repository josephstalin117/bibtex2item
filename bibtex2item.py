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
    entry_type = re.search(r'@(.*?){.*?', r).group(1)
    search_result = re.search(r'(.*?),(.*?$)', r)
    cation_key = re.search(r'{(.*?)$', search_result.group(1)).group(1)
    content = search_result.group(2)
    title = re.search(r'title={(.*?)},',content).group(1)
    authors = re.search(r'author={(.*?)},',content).group(1)
    journal = re.search(r'journal={(.*?)},',content).group(1)
    volume = re.search(r'volume={(.*?)},',content).group(1)
    number = re.search(r'number={(.*?)},',content).group(1)
    pages = re.search(r'pages={(.*?)},',content).group(1)
    year = re.search(r'year={(.*?)},',content).group(1)
    publisher = re.search(r'publisher={(.*?)},',content).group(1)
    print(title)
    exit()
    r = r.split('},')
    for i in r:
        print(i) 
    title = venue = volume = number = pages = year = publisher = month = authors = None
    i = 0
    for i in r:
        if '@' == i[0]:
        #if i.startswith("title"):

            code = line.split('{')[-1][:-1]
            title = venue = volume = number = pages = year = publisher = month = authors = None
            output_authors = []
            i += 1
    while i < len(r) and '@' not in r[i]:
        line = r[i].strip()
        #print(line)
        if line.startswith("title"):
            title = line.split('{')[-1][:-2]
        elif line.startswith("journal"):
            venue = line.split('{')[-1][:-2]
        elif line.startswith("volume"):
            volume = line.split('{')[-1][:-2]
        elif line.startswith("number"):
            number = line.split('{')[-1][:-2]
        elif line.startswith("pages"):
            pages = line.split('{')[-1][:-2]
        elif line.startswith("year"):
            year = line.split('{')[-1][:-2]
        elif line.startswith("publisher"):
            publisher = line.split('{')[-1][:-2]
        elif line.startswith("author"):
            authors = line[line.find("{")+1:line.rfind("}")]
            for LastFirst in authors.split('and'):
                lf = LastFirst.replace(' ', '').split(',')
            if len(lf) != 2: continue
            last, first = lf[0], lf[1]
            output_authors.append("{}, {}.".format(last.capitalize(), first.capitalize()[0]))
        i += 1


def parse_conference(bibtex):
    bibtex = bibtex.readlines()
    # print(bibtex)
    # r = bibtex.split('\n')
    r = bibtex
    i = 0
    while i < len(r):
        line = r[i].strip()
    if not line: i += 1
    if '@' == line[0]:
        code = line.split('{')[-1][:-1]
        title = venue = volume = number = pages = year = publisher = month = authors = None
        output_authors = []
        i += 1
    while i < len(r) and '@' not in r[i]:
        line = r[i].strip()
        #print(line)
        if line.startswith("title"):
            title = line.split('{')[-1][:-2]
        elif line.startswith("journal"):
            venue = line.split('{')[-1][:-2]
        elif line.startswith("volume"):
            volume = line.split('{')[-1][:-2]
        elif line.startswith("number"):
            number = line.split('{')[-1][:-2]
        elif line.startswith("pages"):
            pages = line.split('{')[-1][:-2]
        elif line.startswith("year"):
            year = line.split('{')[-1][:-2]
        elif line.startswith("publisher"):
            publisher = line.split('{')[-1][:-2]
        elif line.startswith("author"):
            authors = line[line.find("{")+1:line.rfind("}")]
            for LastFirst in authors.split('and'):
                lf = LastFirst.replace(' ', '').split(',')
            if len(lf) != 2: continue
            last, first = lf[0], lf[1]
            output_authors.append("{}, {}.".format(last.capitalize(), first.capitalize()[0]))
        i += 1


def bibtex2bibiterm(bibtex):
    print("\\bibitem{%s}" % code)
    if len(output_authors) == 1:
        print(output_authors[0] + " {}. ".format(title),)
    else:
        print(", ".join(_ for _ in output_authors[:-1]) + " & " + output_authors[-1] + " {}. ".format(title),)
    if venue:
        print ("{{\\em {}}}.".format(" ".join([_.capitalize() for _ in venue.split(' ')])),)
    if volume:
        sys.stdout.write(" \\textbf{{{}}}".format(volume))
    if pages:
        sys.stdout.write(", {}".format(pages) if number else " pp. {}".format(pages))
    if year:
        sys.stdout.write(" ({})".format(year))
    if publisher and not venue:
      print("({},{})".format(publisher, year))


if __name__ == '__main__':
    bibs = parse_bibs("./gatattn.bib")
    #print(bibs)
    parse_article(bibs[0])
    