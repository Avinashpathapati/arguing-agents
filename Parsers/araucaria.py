# Parser for auracaria dataset
import json
import os

# by default this is meant to be run as an import from the main file meaning that the working directory is alredy one level up
path_to_corpus = 'Corpora/araucaria/'

if __name__ == "__main__":
	# if this is run as the main file, the path to corpus is different than when its run from the main file
	path_to_corpus = '../Corpora/araucaria'

class t_lPair():
	# object for a training/label pair
	def __init__(self,pairID):
		self.ID = pairID
		self.parse()
		self.checkMissing()

	def parse(self):
		base_path = path_to_corpus + "nodeset" + str(self.ID)
		# storing plain text sentences in a string
		text_path = base_path + ".txt"
		# Initialized as none so its easy to spot missing values
		self.plain = None
		self.labeled = None
		if os.path.isfile(text_path):
			with open(text_path,'r') as f:
				self.plain = f.read()
			json_path = base_path + ".json"
			with open(json_path,'r') as f: # don't use 'rb' as a read option, the json parser can't handle that
				self.labeled = json.load(f)

	def checkMissing(self):
		# checks for missing labels, we can't use an object with missing labels
		if(self.labeled == None):
			# only need to check this condition because the object will not parse if the text is missing
			print('label is missing for ID ' + str(self.ID))
