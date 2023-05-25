import nltk
from nltk.chat.util import Chat, reflections

reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}

pairs = [

    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name ?",
        ["I am a bot created by Analytics Dnyaneshwari. you can call me crazy!",]
    ],
    [
        r"how are you ?",
        ["I'm doing good n How about You ?",]
    ],

    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],

    [
        r"(.*) age?",
        ["I'm a computer program dudenSeriously you are asking me this?",]
    ],

    [
        r"(.*) created ?",
        ["Dnyaneshwari created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Indore, Madhya Pradesh',]
    ],


    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Roony"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
    ],

    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
]

def chat():
    print("Hi! I am a chatbot created by Analytics Dnyaneshwariwhat  for your service")
    chat = Chat(pairs, reflections)
    chat.converse()
#initiate the conversation
if __name__ == "__main__":
    chat()
