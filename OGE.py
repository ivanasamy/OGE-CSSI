import requests
import random
headers = {'content-type': 'application/json', "Ocp-Apim-Subscription-Key": "3338f3285193465e907eb03a5b2b214a", "Accept": "application/json"}
input = "I love life. I am so happy!"

request_body = {
     "documents": [
         {
             "language": "en",
             "id": "1",
             "text": input #what input text is called
         }
     ]
 }


sentiment_call = requests.post('https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment', json= request_body, headers = headers)
sentiment = sentiment_call.json()["documents"][0]["score"]


negative_responses = ["As Willie Nelson once said, 'Keep your face to the sunshine and you cannot see a shadow.'", "As said by the Dalai Lama, 'In order to carry a positive action we must develop here a positive vision.'", "I am sorry about how you feel. A quote I really enjoy is one said by Mewtwo from Pokemon: 'I see now that the circumstances of one’s birth are irrelevant. It is what you do with the gift of life that determines who you are'", "Your feelings are unfortunate, and I would suggest this quote by Martian Manhunter: 'The future is worth it. All the pain. All the tears. The future is worth the fight'"]

neutral_responses = ["A quote I believe applies to a lot of what we do in life is 'If something is too hard, either you are not doing it right or it is not worth doing'", "The opportunity for success is there, you just need to acknowledge its presence and grasp it" , "In anything you do, you are only as good as you think you are."]

positive_responses = ["Congratulations! You seem to be happy and that’s great! Life is short so enjoying it to its fullest is something special!",
"Your happiness is something to be admired! You’re so lucky that things are working out in your life and I hope that things continue to work out!", "That’s wonderful! As an experienced giver of relationship advice, it is always great to hear about people whose lives are filled with joy", "I’m so happy for you! Your joy brings me joy as well!", "Good for you! May happiness forever be in your life!"]

def responses (sentiment):
    if sentiment > 0 and sentiment <0.3:
        return negative_responses[random.randint(range(len(neutral_responses)))]
    elif sentiment >= 0.3 and sentiment <0.7:
        return neutral_responses[random.randint(range(len(neutral_responses)))]
    else:
        return positive_responses[random.randint(range(len(positive_responses)))]

print responses(sentiment)
