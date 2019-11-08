from utility import deaccent
import os
import xml.etree.cElementTree as Et

# go to correct directory, by default, place the Perseus folder in the working folder
homeFolder = os.getcwd()
perseusFolder = os.path.join(os.getcwd(), '1.0 Original')
indir = os.listdir(perseusFolder)

# iterate through files in directory
for file in indir:
    os.chdir(perseusFolder)
    print(file)
    # parse the XML
    tree = Et.parse(file)

    # for each file, iterate through all words, deacent
    for logos in tree.iter('word'):
        accentedWord = logos.get('form')
        unaccentedWord = deaccent(accentedWord).lower()
        logos.set('form', unaccentedWord)
        accentedLemma = logos.get('lemma')
        unaccentedLemma = deaccent(accentedLemma).lower()
        logos.set('lemma', unaccentedLemma)

    os.chdir(homeFolder)
    tree.write(file, encoding='UTF-8')
