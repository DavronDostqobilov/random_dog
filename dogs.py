from pprint import pprint
import time
import requests
TOKEN ='6107593018:AAEUBCT15POSGPilNPZ4ucoFv_3AsWHgkEE'
#GET Updates
def get_updates():
    r=requests.get(f'https://api.telegram.org/bot{TOKEN}/GetUpdates')
    data=r.json()['result'][-1]
    return data
def get_dogs():
    r=requests.get('https://random.dog/woof.json/')
    dog=r.json()['url']
    return dog
def send_photo(chat_id,photo):
    param={'chat_id':chat_id,
           'photo':photo
          }

    r=requests.get(f'https://api.telegram.org/bot{TOKEN}/sendPhoto',params=param)
    ans=r.json()
    return ans
def send_message(chat_id,text):
    param={'chat_id':chat_id,
           'photo':text
          }

    r=requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage',params=param)
    ans=r.json()
    return ans
last_updates_id=-1
while True:
        dogs=get_dogs()
        upp=get_updates()
        chat_id=upp['message']['chat']['id']
        updates_id=upp['update_id']
        if updates_id!=last_updates_id:
            text=upp['message']['text']

            if text=='/dog':
                send_photo(chat_id,dogs)
            last_updates_id=updates_id
        time.sleep(2)