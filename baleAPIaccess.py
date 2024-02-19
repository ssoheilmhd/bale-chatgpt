import requests

def GetUpdateFromUsers(Method):
    """
    This is created to find new user's message
    """
    url = 'https://tapi.bale.ai/bot1064197082:x1cIcTfyNrXxBSFfPUUaxG2Ybv5BOe9bLIgXcvbI/%s' % Method
    #-1 in offset is last message which is sent by users
    payload = {'offset': -1 }
    response = requests.get(url,params=payload)
    chat_id = response.json()['result'][0]['message']['from']['id']
    message_id = response.json()['result'][0]['message']['message_id']
    text = response.json()['result'][0]['message']['text']
    return message_id,chat_id,text

def AnswerToUser(Method,chat_id,text,message_id):
    """
    This function is created to send the chatgpt's response to the user
    """
    url = 'https://tapi.bale.ai/bot1064197082:x1cIcTfyNrXxBSFfPUUaxG2Ybv5BOe9bLIgXcvbI/%s' % Method
    payload = { 'chat_id':chat_id, 'text':text, 'reply_to_message_id':message_id }
    response = requests.post(url,params=payload)
    print (response)
