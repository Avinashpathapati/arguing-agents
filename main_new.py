# Start of the prject
# Data is in plain text and Json format
# Use Spacy for linguistic processing, pos tagging to add features and such

# TODO - build quick test parser of training data. Json specifically. DONE AND TESTED
# TODO - identify missing nodeset IDs because its fucking up the program (check file existance before reading in parse()?)

import os
from Parsers import lstm_new

path_to_corpus = os.getcwd() + '/Corpora'

#path_to_corpus = "/Users/sandy/Downloads/UKP Sentential Argument Mining Corpus/data/complete"
#path_to_corpus = "/Users/sandy/Downloads/UKP Sentential Argument Mining Corpus/data/complete"
##path_to_corpus = "/Users/sandy/Downloads/"
#arConstObj = araucaria_new.ConstDataSet()
#
##arConstObj.readFile("0", path_to_corpus)
##arConstObj.readFile("1", path_to_corpus)
#arConstObj.readFile("2",  path_to_corpus)
#arConstObj.extractFeatures()
##arConstObj.extractVerbs()
#arConstObj.buildSvm()
#print(len(data))
#print(data[0].plain)
word2vec = lstm_new.ConstWord2Vec()
#word2vec.readTsvFileAndConstructDataset(path_to_corpus)
word2vec.load_model(["People are going to do it anyway"],[['0','1']])