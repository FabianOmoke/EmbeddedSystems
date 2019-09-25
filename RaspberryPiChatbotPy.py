import random

random_replies = ['Oh really?', 'Are you sure about that?', 'Perhaps…', 'I don’t think so']

chat_dict = {'happy': 'I’am happy today too', 'sad': 'Be happy, life is good', 'computer': 'Computers will take over the world!'}


def dictionary_check(message):
    message = message.lower()
    user_words = message.split()
    smart_replies = []

    for word in user_words:
        if word in chat_dict:
            answer = chat_dict.__getitem__(word)
            smart_replies.append(answer)

    if smart_replies:
        reply_chose = random.randint(0, len(smart_replies)-1)
        return smart_replies[reply_chose]
    else:
        return ""


print(len(random_replies), '\n')
print("What would you like to talk about?")
user_talks = ""

while user_talks != 'bye':
    user_talks = ""
    while user_talks == "":
        user_talks = input("What would you like to say")
    smart_response = dictionary_check(user_talks)
    if smart_response:
        print(smart_response)
    else:
        reply_chosen = random.randint(1, len(random_replies) )-1
    print(random_replies[reply_chosen])
    random_replies[reply_chosen] = user_talks
print("Goodbye. Thanks for chatting today!")