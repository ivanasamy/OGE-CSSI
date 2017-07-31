import requests
headers = {'content-type': 'application/json', "Ocp-Apim-Subscription-Key": "3338f3285193465e907eb03a5b2b214a", "Accept": "application/json"}

input = "Dear Oge, I am so upset that my boyfriend left me for another girl. What do I do?"

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
sentiment_1 = requests.post('https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment', json= request_body, headers = headers)
sentiment = sentiment_1.json()["documents"][0]["score"]
#keywords = keyword.json()["documents"][0]["keyPhrases"]



#print(keywords.text)
