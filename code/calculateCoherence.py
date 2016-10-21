# -*- coding: utf-8 -*-

import logging, os

from gensim import corpora, models, matutils

from code.util import loadFileIntoList

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def calculateCoherence(config):

    lsaModel = models.LsiModel.load(config['LSA']['modelFileLocation'])

    dictionary = corpora.Dictionary.load(config['corpus']['corpusFolderLocation'] + 'corpus.dict')

    corpus = corpora.MmCorpus(config['corpus']['corpusFolderLocation'] + 'corpus.mm')

    tfidf = models.TfidfModel(corpus)

    for dataset in config['corpus']['datasets']:

        for transcriptPath in os.listdir(dataset['path']):
            document = loadFileIntoList(dataset['path'] + "/" + transcriptPath,
                                        dataset['transcriptColumn'], dataset['delimiter'],
                                        dataset['rowsToSkip'], config['corpus']['sentenceSplitting'], config['corpus']['stopwords'])

            with open(config['coherence']['outputFolderLocation'] + transcriptPath + "_results_lsa.tsv", 'w') as outputFile:

                # write header
                outputFile.write("coherence to previous sentence(s)\tpreprocessed sentence\tfull sentence\tcorresponding turn\n")

                lastSentencesLSAList = []
                for sentence in document:
                    if " ".join(sentence[0]):

                        sentenceBow = dictionary.doc2bow(sentence[0])

                        weightIndex = 1
                        simLSA = 0
                        weightNormalizer = 0
                        for el in lastSentencesLSAList:
                            simLSA += 1/weightIndex * matutils.cossim(lsaModel[tfidf[sentenceBow]], el)
                            weightNormalizer += 1/weightIndex
                            weightIndex += 1

                        if weightNormalizer > 0:
                            simLSA /= weightNormalizer

                        lastSentencesLSAList.insert(0, lsaModel[tfidf[sentenceBow]])

                        if len(lastSentencesLSAList) > config['coherence']['slidingWindow']:
                            del lastSentencesLSAList[-1]

                        outputFile.write(str(simLSA)+"\t")
                        outputFile.write(" ".join(sentence[0])+"\t")
                        outputFile.write(" ".join(sentence[1])+"\t")
                        outputFile.write(sentence[2]+"\n")