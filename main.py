# -*- coding: utf-8 -*-

from code.buildCorpus import buildCorpus
from code.buildLSAmodel import buildLSAmodel
from code.calculateCoherence import calculateCoherence
from code.config import loadConfig

if __name__ == "__main__":

    config = loadConfig()
    buildCorpus(config)
    buildLSAmodel(config)
    calculateCoherence(config)