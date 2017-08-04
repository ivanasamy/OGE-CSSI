# -*- coding: utf-8 -*-﻿
from __future__ import unicode_literals
import random
import urllib
import json
from google.appengine.api import urlfetch
emoji_dic = {
    "happy": "😀",
    "winking": "😉",
    "kissing": "😗",
    "smirking": "😏",
    "crying": "😢",
    "woman": "👩",
    "peach": "🍑",
    "eggplant": "🍆"
    }

headers = {'content-type': 'application/json', "Ocp-Apim-Subscription-Key": "3338f3285193465e907eb03a5b2b214a", "Accept": "application/json"}

def adjust_input(i):
    build = []
    for ele in i:
        low = ele.lower()
        if low in emoji_dic:
            build.append(emoji_dic[low])
        else:
            build.append(ele)
    sentence = " ".join(build)
    return sentence


def oge_response(response):
    parsed_res = response.split()
    if len(parsed_res) == 0:
        return "How can Oge give advice if you don't write anything?"
    request_body = { "documents": [{"language": "en",
         "id": "1",
         "text": response,
        }]}

    url = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment'


    response = urlfetch.fetch(
                 url,
                 headers=headers,
                 method='POST',
                 payload=json.dumps(request_body)
               )

    sentiment_json = json.loads(response.content)
    sentiment = sentiment_json["documents"][0]["score"]

    negative_responses = ["As Helen Keller once said, Keep your face to the sunshine and you cannot see a shadow.",
    "As said by the Dalai Lama, In order to carry a positive action we must develop here a positive vision.", "I am sorry about how you feel. A quote I really enjoy is one said by Mewtwo from Pokemon, I see now that the circumstances of one's birth are irrelevant. It is what you do with the gift of life that determines who you are",
    "Your feelings are unfortunate, and I would suggest this quote by Martian Manhunter, The future is worth it. All the pain. All the tears. The future is worth the fight", "If you love someone, set them free. If they come back they're yours; if they don't they never were. - Richard Bach", "Truth is everybody is going to hurt you: you just gotta find the ones worth suffering for. - Bob Marley", "Never love someone who treats you like you are ordinary - Oscar Wilde"]

    neutral_responses = ["A quote I believe applies to a lot of what we do in life is 'If something is too hard, either you are not doing it right or it is not worth doing'", "The opportunity for success is there, you just need to acknowledge its presence and grasp it" , "In anything you do, you are only as good as you think you are.", "Anything is possible when you have inner peace - Master Shifu(Kung Fu Panda)","To laugh at yourself is to love yourself - Mickey Mouse", "Sucking at something is the first step to becoming sorta good at something - Jake from Adventure Time"]
#
    positive_responses = ["Congratulations! You seem to be happy and that’s great! Life is short so enjoying it to its fullest is something special!", "Your happiness is something to be admired! You’re so lucky that things are working out in your life and I hope that things continue to work out!", "That’s wonderful! As an experienced giver of relationship advice, it is always great to hear about people whose lives are filled with joy", "I’m so happy for you! Your joy brings me joy as well!", "Good for you! May happiness forever be in your life!"]


    for ele in parsed_res:
        if ele.lower() in emoji_dic:
            return "I'm sorry, did you mean \"%s\"" % (adjust_input(parsed_res))
    if sentiment > 0 and sentiment <0.33:
        return "%s <br><br>Also, you shouldn't have to be alone during this time. I would suggest getting a cat to keep you company! Please visit our Ways to Be Happy Page!"% (negative_responses[random.randint(0, len(negative_responses)-1)])
    elif sentiment >= 0.33 and sentiment <0.67:
        return "NEUTRAL"
    else:
        return positive_responses[random.randint(0, len(positive_responses)-1)]
