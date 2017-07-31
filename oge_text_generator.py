# random text generator
# makes oge response generator
import random

def split_words(inputed):
    # input is a sentence, output is a list with each word in the sentence an element
    split = inputed.split()
    return split

def two_words(text_list):
    #this function takes the list of words from the previous function as its input and produces a dictionary with the keys being every two consecutive words and the values of the keys being a list of the words that follow those two words
	dictionary = {}
	for index in range(0, len(text_list) - 2):
		word1=text_list[index]
		word2=text_list[index + 1]
		word3=text_list[index + 2]
		if (word1, word2) in dictionary:
			dictionary[word1, word2].append(word3)
		else:
			dictionary[word1, word2] = [word3]
	return dictionary

def one_word(text_list):
    dictionary = {}
    for index in range(0, len(text_list) - 1):
		word1=text_list[index]
		word2=text_list[index + 1]
		if (word1) in dictionary:
			dictionary[word1].append(word2)
		else:
			dictionary[word1] = [word2]
    return dictionary

def Oge_Response(inputed):
    # input is the input text given by user, aka the "Dear Oge"
    individual_words = split_words(inputed)
    oneword = one_word(individual_words)
    twowords = two_words(individual_words)
    print twowords
    print oneword


Oge_Response("I am sad. I am depressed. I am lonely")
