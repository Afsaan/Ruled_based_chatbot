from nltk.chat.util import Chat, reflections


print(reflections)

# dummy reflection
my_dummy_reflections= {
    "go"     : "gone",
    "hello"    : "hey there"
}

#default message at the start of chat
print("Hi, I'm thecleverprogrammer and I like to chat\nPlease type lowercase English language to start a conversation. Type quit to leave ")
#Create Chat Bot
chat = Chat(pairs, reflections)

#Start conversation
chat.converse()