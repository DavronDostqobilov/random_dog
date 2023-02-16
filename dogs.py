import time
import requests
TOKEN ='6138073029:AAEKI-9AA9pxG_goL9l8soAhff0GD0IqX7g'
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
def send_message(chat_id):
    keyboard=[[{'text':'dog🐶'}],[{'text':'cat😺'}]]
    reply_markup={'keyboard':keyboard}
    param={
        'chat_id':chat_id,
        'text':'Pastki panelga o`ting',
        'reply_markup':reply_markup

    }

    r=requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',json=param)
    ans=r.json()['result']
    return ans
last_updates_id=-1
while True:
        dogs=get_dogs()
        cats=get_cats()
        upp=get_updates()
        print(upp)
        chat_id=upp['message']['chat']['id']
        text=upp['message']['text']
        updates_id=upp['update_id']

        
        if updates_id!=last_updates_id:
            if text=='/start':
                send_message(chat_id)
            if text=='dog🐶':
                send_photo(chat_id,dogs)
            if text=='cat😺':
                 send_photo(chat_id,cats)
            last_updates_id=updates_id
        time.sleep(2)