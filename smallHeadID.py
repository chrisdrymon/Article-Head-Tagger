import tensorflow as tf
import pandas as pd
import xml.etree.cElementTree as cET
import os
from collections import Counter

# Go through corpus and make a list of every unique word occurring before ο
filePathDir = os.path.join(os.getcwd(), 'Texts')
statsDir = os.path.join(os.getcwd(), 'Stats')
os.chdir(filePathDir)
passed = 0
passedLemma = 0
formList = []
lemmaList = []
totalPosCounter = Counter()
totalRelCounter = Counter()
for file in os.listdir(filePathDir):
    print(file)
    if file[:6] == 'PROIEL':
        tree = cET.parse(file)
        artPosCounter = Counter()
        artRelCounter = Counter()
        for logos in tree.iter('token'):
            if logos.get('form') in formList:
                passed += 1
            else:
                formList.append(logos.get('form'))
            if logos.get('lemma') in lemmaList:
                passedLemma += 1
            else:
                lemmaList.append(logos.get('lemma'))
            if logos.get('lemma') == 'ο':
                articlePos = logos.get('part-of-speech')
                articleRelation = logos.get('relation')
                if articlePos in artPosCounter.keys():
                    artPosCounter[articlePos] += 1
                else:
                    artPosCounter[articlePos] = 1
                if articleRelation in artRelCounter.keys():
                    artRelCounter[articleRelation] += 1
                else:
                    artRelCounter[articleRelation] = 1
    else:
        tree = cET.parse(file)
        artPosCounter = Counter()
        artRelCounter = Counter()
        for logos in tree.iter('word'):
            if logos.get('form') in formList:
                passed += 1
            else:
                formList.append(logos.get('form'))
            if logos.get('lemma') in lemmaList:
                passedLemma += 1
            else:
                lemmaList.append(logos.get('lemma'))
            if logos.get('lemma') == 'ο':
                articlePos = logos.get('postag')[:1]
                articleRelation = logos.get('relation')
                if articlePos in artPosCounter.keys():
                    artPosCounter[articlePos] += 1
                else:
                    artPosCounter[articlePos] = 1
                if articleRelation in artRelCounter.keys():
                    artRelCounter[articleRelation] += 1
                else:
                    artRelCounter[articleRelation] = 1
    print(artPosCounter)
    print(artRelCounter, '\n')
    totalPosCounter = totalPosCounter + artPosCounter
    totalRelCounter = totalRelCounter + artRelCounter
# Create tensor predicting whether ο is an article or something else according to previous word and next word.
print(len(formList), "unique forms.")
print(passed, "forms repeated.")
print(len(lemmaList), "unique lemmas.")
print(passedLemma, "lemmas repeated.\n")
print('Counter totals:')
print(totalPosCounter)
print(totalRelCounter)
