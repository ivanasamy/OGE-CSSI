import requests
import random
headers = {'content-type': 'application/json', "Ocp-Apim-Subscription-Key": "3338f3285193465e907eb03a5b2b214a", "Accept": "application/json"}

<<<<<<< HEAD
input = "I love life. I am so happy!"
=======
input = "Dear Oge Letter"
>>>>>>> 989b51565a03053a38bd576a6e35cc693027156a

request_body = {
     "documents": [
         {
             "language": "en",
             "id": "1",
             "text": input #what input text is called
         }
     ]
 }


#keyword = requests.post('https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/keyPhrases', json= request_body, headers = headers)
sentiment_call = requests.post('https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment', json= request_body, headers = headers)
sentiment = sentiment_call.json()["documents"][0]["score"]
#keywords = keyword.json()["documents"][0]["keyPhrases"]

negative_responses = []
neutral_responses = []
positive_responses = []

def responses (sentiment):
    if sentiment > 0 and sentiment <0.3:
        return negative_responses[random.randint(range(len(neutral_responses)))]
    elif sentiment >= 0.3 and sentiment <0.7:
        return neutral_responses[random.randint(range(len(neutral_responses)))]
    else:
        return positive_responses[random.randint(range(len(positive_responses)))]

print sentiment
