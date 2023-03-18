#python authomation

#we need textbelt and shedule

#textbelt helps in sending messages

#shedule when we want the message to be executed

# from credentials import mobile_number
import requests
import shedule
import time
def send_message():
    resp=requests.post('https://textbelt.com/text',{
        'mobile_number': 672384579,
        'message': 'hii good morning',
        'key': 'textbelt'
    })
    print(resp.json())

shedule.every(10).seconds.do(send_message)

while True:
    shedule.run_pending()
    time.sleep(1)