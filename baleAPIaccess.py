import requests
import os
from dotenv import load_dotenv
load_dotenv()
baleAPItoken = os.environ['baleAPItoken']
url = f'https://tapi.bale.ai/bot{baleAPItoken}'

def GetUpdateFromUsers(Method):
    """
    This is created to find new user's message
    """
    #-1 in offset is last message which is sent by users
    payload = {'offset': -1 }
    response = requests.get(url+f'/{Method}',params=payload)
    chat_id = response.json()['result'][0]['message']['from']['id']
    message_id = response.json()['result'][0]['message']['message_id']
    text = response.json()['result'][0]['message']['text']
    return message_id,chat_id,text

def AnswerToUser(Method,chat_id,text,message_id):
    """
    This function is created to send the chatgpt's response to the user
    """
    payload = { 'chat_id':chat_id, 'text':text, 'reply_to_message_id':message_id }
    response = requests.post(url+f'/{Method}',params=payload)
    print (response)
