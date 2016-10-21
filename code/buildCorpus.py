# -*- coding: utf-8 -*-

import logging, os
from collections import defaultdict

from gensim import corpora

from code.util import loadFileIntoList

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def buildCorpus(config):

    documents = []

    for dataset in config['corpus']['datasets']:

        for transcriptPath in os.listdir(dataset['path']):
            document = loadFileIntoList(dataset['path'] + "/" + transcriptPath,
                                        dataset['transcriptColumn'], dataset['delimiter'],
                                        dataset['rowsToSkip'], config['corpus']['sentenceSplitting'], config['corpus']['stopwords'])
            for utterance in document:
                documents.append(utterance[0])

    frequency = defaultdict(int)
    for text in documents:
        for token in text:
            frequency[token] += 1

    texts = [[token for token in text] for text in documents]

    dictionary = corpora.Dictionary(texts)
    dictionary.save(config['corpus']['corpusFolderLocation'] + 'corpus.dict')
    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize(config['corpus']['corpusFolderLocation'] + 'corpus.mm', corpus)