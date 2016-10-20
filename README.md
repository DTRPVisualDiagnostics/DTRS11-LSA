# DTRS11-LSA

This is the code for the paper "Combining computational and human analysis to study low coherence in design conversations" by Axel Menning, Bastien Marvin Grasnick, Benedikt Ewald, Andrea Scheer, Franziska Dobrigkeit, Martin Schuessler and Claudia Nicolai for the DTRS11: Design Thinking Research Symposium 2016.

This tool is used to calculate a coherence value between consecutive turns or sentences of transcribed conversations based on Latent Semantic Analysis.

It was built in Python 3 so we advise to also use this version of Python in order to run it. 
If you really need or want to use Python 2 some modifications may be necessary.
 
It is separated into three steps that can be used independently: 

- building the corpus from the transcriptions
- building the LSA model using the corpus 
- calculating the coherence values between sentences or turns using the LSA model

This modularity enables you for example to swap out LSA for another model like LDA or try out different coherence calculations. 
Make sure to only include the steps you want to execute in the main.py file.

In order to run it, first install the dependencies with ```pip install -r requirements.txt``` and then simply executing ```python code/main.py```.

It works with data in a tabular format (csv or tsv) and can be configured by changing the values in the config.json file.

Let's quickly go through the options there:

# Configuration options

__sentenceSplitting__:
Here you can decide whether you want to calculate LSA coherence values based on individual sentences or rather whole turns.

__corpusFolderLocation__:
Where to save the corpus build from all the words in your documents.

__stopwords__:
A list of user-defined stop words that are gonna be added on top of the stopwords from the [Python package stop-words](https://pypi.python.org/pypi/stop-words).

__datasets__:
A list of multiple datasets can be specified to work with. The parameters for them are explained next.

__path__:
The path to the folder in which the files of the dataset are stored.

__transcriptColumn__:
The column of the table in which the textual transcript resides.
 
__delimiter__:
The delimiter of the csv or tsv files used (e.g. "," ";" "\t").

__rowsToSkip__:
How many initial rows need to be skipped before the actual transcript starts (e.g. because they contain meta data or explanations).

__numberOfTopics__:
The amount of dimensions for the LSA model.

__modelFileLocation__:
Where to store the LSA model.

__slidingWindow__:
The amount of preceding turns that are considered for the coherence calculation in a weighted manner (see the paper for more details).
 
__outputFolderLocation__:
Where to store the results of the coherence calculation for each input file.

# Acknowledgements

A lot of thanks go to the developers of the following tools that we used:

### [NLTK](https://github.com/nltk/nltk)

Bird, Steven, Edward Loper and Ewan Klein (2009). Natural Language Processing with Python. O'Reilly Media Inc.

### [Gensim](https://github.com/RaRe-Technologies/gensim)

Rehurek, R., & Sojka, P. (2010). Software framework for topic modelling with large corpora. In In Proceedings of the LREC 2010 Workshop on New Challenges for NLP Frameworks.