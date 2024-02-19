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
    time.sleep(3)
