# -*- coding: utf-8 -*-

import json
from stop_words import get_stop_words

def loadConfig():

    with open('./config.json') as jsonFile:
        config = json.load(jsonFile)

    enStopwords = get_stop_words('en')
    config['corpus']['stopwords'] += enStopwords

    return config