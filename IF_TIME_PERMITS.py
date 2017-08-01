# random text generator
# makes oge response generator
import random

def split_words(inputed):
    # input is a sentence, output is a list with each word in the sentence an element
    split = inputed.split()
    return split
#hello
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
    oge_output = ""
    cat_keys = ["sad.","sad", "depressed.", "depressed", "lonely", "lonely.", "upset", "upset.", "mad", "mad.", "frustrated", "fristrated."]
    happy_keys = ["glad", "glad.", "happy", "happy.", "relieved", "relieved."]
    cheated_keys = ["cheat", "cheated.", "cheated", "cheating"]
    communication_keys = ["talking", "unresponsive", "avoiding", "quiet"]
    generic_response = "You know, I don't know what to tell you. Maybe you should see someone else about this, Oge doesn't have all the answers. "
    cheated_response = "I cannot BELIEVE they cheated on you! You must be a wreck! You know what would make you feel better? Adopting a beautiful cat who needs a home. Check here for cats. "
    cheating_response = "Are you absolutely sure that they're cheating on you? "
    cheater_repsonse = "SHAME ON YOU! How dare you cheat on your significant other! Do you have any idea what they must be going through? I can't give advice to cheaters, it's against my protocol. "
    communication_response_cheater = "You know, maybe they're not talking to you because you CHEATED on them. Just a thought. "
    communication_response_cheated = "I think you need to talk to them. Sometimes there can be a lot of miscommunication in a relationship. "
    happy_response = "If you're happy, why do you need my help? "
    getting_over_it_response = "Glad you're looking to get over them! You know what I think would help, adopting a beautiful cat who needs a home! Check here for more details. "
    cat_response = "It sounds like you've been a little down. You know what'll make you feel better? Adoption. Specifically, adopting a cat. "
    sympathetic_starters = ["I'm so sorry to hear that. ", "It's a shame that you've been going through this. ", "You know, my grandma has a saying: Everything happens for a reason. "]
    individual_words = split_words(inputed)
    oneword = one_word(individual_words)
    twowords = two_words(individual_words)
    oge_output+= sympathetic_starters[random.randint(0,len(sympathetic_starters)-1)]
    if ("I", "am") in twowords:
        for key in twowords["I", "am"]:
            if key in cat_keys:
                oge_output+= cat_response
                cat_keys = []
            if key in cheated_keys:
                oge_output+= cheater_repsonse
    if twowords("boyfriend", "was") in cheated_keys:
        oge_output += cheated_response



    print oge_output


Oge_Response("I am sad. I am depressed. I am lonely. I am cheating on my boyfriend.")
