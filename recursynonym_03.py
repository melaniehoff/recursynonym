
import unicodedata
import urllib
import json
import sys
import random

relationship = 'synonym'
word = sys.argv[1]
params = {
	'useCanonical': 'false',
	'limitPerRelationshipType' : 100,
	'relationshipTypes': relationship,
	'api_key': '95267802aa91116df6707075b55046dba203deffbb5614ad3'
}

def unUnicode(s):
	try:
		return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')
	except:
		return s

def getSynlist(word):
	url_path = "http://api.wordnik.com:80/v4/word.json/" + unUnicode(word) + "/relatedWords?"
	query_s = urllib.urlencode(params)
	url = url_path + query_s
	raw_data = urllib.urlopen(url).read()
	data = json.loads(raw_data)

	# print "hey data: {}".format(data)
	# print "word: {}".format(word)

	if isinstance(data, list):

		if data:
			if data[0]['words']:
				related_words = data[0]['words']
				# print "hey related: {}".format(related_words)

				return related_words

def getFirstNewWord(totallist, listofsyn):
	newword = ""
	random.shuffle(listofsyn)

	for aWord in listofsyn:

		if aWord not in totallist:
			# ///////pruning
			if not getSynlist(aWord):
				continue
			#///////////
		newword = aWord
			# print "new word !!!!!!!!!!!" + newword
		return newword
		break


newword = word
totalList = []
totalList.append(word)

print ('\n' * 20)
print ('    				   ' + word.upper() + '\n')
for x in range (0,100):

	listofSyn = getSynlist(newword)

	if listofSyn == None:
		print ('\n' * 20)
		break
	else:
		prevword = newword
		newword = getFirstNewWord(totalList, listofSyn)

		if newword != None:
			print ("				becomes " + newword + '\n'),
		else:
			print ('\n' * 15 + "x" + '\n')
			break

		totalList.append(newword)
