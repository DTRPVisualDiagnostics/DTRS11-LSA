# -*- coding: utf-8 -*-

import re, csv

from nltk.stem.porter import PorterStemmer

from nltk.tokenize import sent_tokenize

pStemmer = PorterStemmer()

def cleanLine(line, stopwords, move=""):
	line = line.replace("THE COMPANY", "paulmotors")
	line = line.replace("COMPANY", "paulmotors")
	lowerLine = line.lower()
	cleanedLine = re.sub(r'\([^)]*\)', ' ', lowerLine)
	cleanedLine = re.sub(r'\-[^-]*\-', ' ', cleanedLine)
	cleanedLine = re.sub(r'\d+', ' ', cleanedLine)
	tokens = cleanedLine.split(" ")
	stoppedTokens = [i for i in tokens if not i in stopwords]
	cleanedLine = " ".join(stoppedTokens)
	cleanedLine = cleanedLine.replace("["," ")
	cleanedLine = cleanedLine.replace("]"," ")
	cleanedLine = cleanedLine.replace("("," ")
	cleanedLine = cleanedLine.replace(")"," ")
	cleanedLine = cleanedLine.replace("{"," ")
	cleanedLine = cleanedLine.replace("}"," ")
	cleanedLine = cleanedLine.replace("/"," ")
	cleanedLine = cleanedLine.replace(":"," ")
	cleanedLine = cleanedLine.replace("."," ")
	cleanedLine = cleanedLine.replace("!"," ")
	cleanedLine = cleanedLine.replace("?"," ")
	cleanedLine = cleanedLine.replace(","," ")
	cleanedLine = cleanedLine.replace("-"," ")
	cleanedLine = cleanedLine.replace("_"," ")
	cleanedLine = cleanedLine.replace("–"," ")
	cleanedLine = cleanedLine.replace("-"," ")
	cleanedLine = cleanedLine.replace("–"," ")
	cleanedLine = cleanedLine.replace("+"," ")
	cleanedLine = cleanedLine.replace("“"," ")
	cleanedLine = cleanedLine.replace("”"," ")
	cleanedLine = cleanedLine.replace("„"," ")
	cleanedLine = cleanedLine.replace("…"," ")
	cleanedLine = cleanedLine.replace("<"," ")
	cleanedLine = cleanedLine.replace(">"," ")
	cleanedLine = cleanedLine.replace("‘"," ")
	cleanedLine = cleanedLine.replace("’"," ")
	cleanedLine = cleanedLine.replace("\""," ")
	cleanedLine = cleanedLine.replace("\'"," ")
	cleanedLine = cleanedLine.replace("\n"," ")
	cleanedLine = cleanedLine.replace("'","\"")
	while "xxx" in cleanedLine:
		cleanedLine = cleanedLine.replace("xxx","xx")
		cleanedLine = cleanedLine.replace("xx"," ")
	tokens = cleanedLine.split(" ")
	stoppedTokens = [i for i in tokens if not i in stopwords if i]
	stemmedTokens = [pStemmer.stem(i) for i in stoppedTokens if i]
	finalTokens = [i for i in stemmedTokens if i != "s" and i != "t"]
	finalLine = " ".join(finalTokens)
	lowerLine = lowerLine.replace("\n"," ")
	lowerLine = lowerLine.replace("\t"," ")
	move = move.replace("\n"," ")
	move = move.replace("\t"," ")
	return (finalLine.rstrip('\n').split(" "), lowerLine.rstrip('\n').split(" "), move.rstrip('\n'))

def loadFileIntoList(path, index, delimiter, skipLines, sentenceSplitting, stopwords):
	doc = []
	with open(path, 'rt') as csvfile:
		csvReader = csv.reader(csvfile, delimiter=delimiter)
		for x in range(skipLines):
			next(csvReader,None)
		for row in csvReader:
			if len(row) >= index and row[index]:
				if sentenceSplitting:
					splitSentences = sent_tokenize(row[index])
					for sentence in splitSentences:
						cleanedLine = cleanLine(sentence, stopwords, row[index])
						if (cleanedLine[0] != ['']):
							doc.append(cleanedLine)
				else:
					cleanedLine = cleanLine(row[index], stopwords)
					if (cleanedLine[0] != ['']):
						doc.append(cleanedLine)
	return doc