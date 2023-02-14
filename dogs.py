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
def get_cats():
    r=requests.get('https://aws.random.cat/meow')
    cat=r.json()['file']
    return cat
     
def send_photo(chat_id,photo):
    param={'chat_id':chat_id,
           'photo':photo
          }

    r=requests.get(f'https://api.telegram.org/bot{TOKEN}/sendPhoto',params=param)
    ans=r.json()
    return ans
def send_message():
    keyboard=[[{'text':'dog🐶'}],[{'text':'cat😺'}],[{'text':'_🐶_Tepaga bosing_😺_'}]]
    reply_markup={'keyboard':keyboard}
    param={
        'chat_id':get_updates()['message']['chat']['id'],
        'text':'/start',
        'reply_markup':reply_markup

    }

    r=requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',json=param)
    ans=r.json()['result']
    return ans
print(send_message())
last_updates_id=-1
while True:
        dogs=get_dogs()
        cats=get_cats()
        upp=get_updates()
        chat_id=upp['message']['chat']['id']
        updates_id=upp['update_id']
        if updates_id!=last_updates_id:
            text=upp['message']['text']
            print(chat_id)
            if text=='dog🐶':
                send_photo(chat_id,dogs)
            if text=='cat😺':
                 send_photo(chat_id,cats)
            last_updates_id=updates_id
        time.sleep(2)