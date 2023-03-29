#python authomation

#we need textbelt and shedule

#textbelt helps in sending messages

#shedule when we want the message to be executed

from credentials import mobile_number
import requests

def send_message():
    resp=requests.post('https://textbelt.com/text',{
        'mobile_number': 672384579,
        'message': 'hii good morning',
        'key': 'texbelt'
    })
    print(resp.json())