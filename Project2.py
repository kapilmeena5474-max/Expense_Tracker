#AI Chatbot
import datetime
import time
name= input("Enter your name : ")
presentHour = datetime.datetime.now().hour

if (5<= presentHour <= 11):
    print("Good Morning ", name)
elif (11<= presentHour <=17):
    print("Good Afternoon ", name)
elif (17<= presentHour <= 20):
    print("Good Evening ", name)
else:
    print ("Good Night ", name)    


print("Namaste! Welcome to Your own Chatbot")
print("You can ask me the basic question, And type 'Bye' to exit from the bot")

#Chatbot Memory Creation

responses = {
    "hello": "HI , welcome. How can I help you",
    "how are yo" : "I am very fine. Thanks to ask",
    "who are you" : "I am smart AI chatbot",
    "motivate me" : "keep going. You will achieve whatever you wants",
    "You are not true" : "Sorry for that! I will work on Myself",
    "How to become rich": "JUST GO and STUDY",
    "How much stars in universe": "Why don'nt you count it by yourself"
    
}

#Method to get response of question

def get_response_bot(userquestion):
    userquestion = userquestion.lower()
    for eachkey in responses:
        if eachkey in userquestion:
            return responses[eachkey]
    return "I am not Able to tell that yet...... But I will work on myself to know it"

while True:
    userinput = input("Please ask your question : ")
    replay = get_response_bot(userinput)
    print("Bot Response : ", replay)

    if "bye" in userinput.lower():
        break
