from utility import deaccent
import os
import xml.etree.cElementTree as Et

# go to correct directory
homeFolder = os.getcwd()
PROIELFolder = os.path.join(os.getcwd(), 'PROIEL')
indir = os.listdir(PROIELFolder)

# iterate through files in directory
for file in indir:
    os.chdir(PROIELFolder)
    print(file)
    # parse the XML
    tree = Et.parse(file)

    # for each file, iterate through all words, deacent
    for logos in tree.iter('token'):
        if 'form' in logos.attrib:
         #   citation = logos.get('citation-part')
            accentedWord = logos.get('form')
           # print(accentedWord)
            unaccentedWord = deaccent(accentedWord).lower()
            logos.set('form', unaccentedWord)
            accentedLemma = logos.get('lemma')
            unaccentedLemma = deaccent(accentedLemma).lower()
            logos.set('lemma', unaccentedLemma)

    os.chdir(homeFolder)
    tree.write(file, encoding='UTF-8')
