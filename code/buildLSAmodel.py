# -*- coding: utf-8 -*-

import logging
from gensim import corpora, models

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def buildLSAmodel(config):
    dictionary = corpora.Dictionary.load(config['corpus']['corpusFolderLocation'] + 'corpus.dict')
    corpus = corpora.MmCorpus(config['corpus']['corpusFolderLocation'] + 'corpus.mm')

    tfidf = models.TfidfModel(corpus)
    corpusTfidf = tfidf[corpus]

    lsaModel = models.LsiModel(corpusTfidf, id2word=dictionary, num_topics=config['LSA']['numberOfTopics']) # initialize an LSI transformation

    lsaModel.save(config['LSA']['modelFileLocation'])