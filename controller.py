import time
from baleAPIaccess import *
from chatgptCaller import *

check_message_id = 'null'

while True:
    message_id,chat_id,text = GetUpdateFromUsers("getUpdates")
    if check_message_id == message_id:
        continue
    check_message_id = message_id
    ChatgptResponse = SendQuestionToChatgpt(text)
    AnswerToUser("sendMessage",chat_id,ChatgptResponse,message_id)
    #Chatgpt API free version has a certain limit on the number of requests, you can only send 20 requests per minute
    #I decided to reply the last user after 3 seconds. It helps me to have maximum requests (20) in a minute
    #It's cristal clear that if you buy a good license you can change this line.
    time.sleep(3)
