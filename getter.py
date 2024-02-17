import requests

def baleAPIcaller(Method):
    """
    This function converts the input address into coordinates, this way we can find the source and destination for traffic analyzer
    """
    url = 'https://tapi.bale.ai/bot1064197082:x1cIcTfyNrXxBSFfPUUaxG2Ybv5BOe9bLIgXcvbI/%s' % Method
    payload = {'offset':-1}
    #payload = { 'chat_id':'1183767264', 'text':'payame 2 salam chetori man bot hastam', 'reply_to_message_id':4 }
    response = requests.post(url,params=payload)
    test = response.json()
    print (test)


inp= "getUpdates"
#inp = "sendMessage"
baleAPIcaller(inp)
