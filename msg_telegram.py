
import json
import requests

def send_telegram(message: str, chat_id: str, tokenBot):  
    proxies = None 
    headers = {'Content-Type': 'application/json', 'Proxy-Authorization': 'Basic base64'} 
    data_dict = {'chat_id': chat_id, 'Document': message, 'disable_notification': True}
    data = json.dumps(data_dict) 
    print(data_dict)
    url = f'https://api.telegram.org/bot{tokenBot}/sendDocument' 
    response = requests.post(url, data=data, headers=headers, proxies=proxies, verify=False) 
    return response     

def send_mensaje(archivo: str, chat_id: str, tokenBot,info_msg):
    token_bot = tokenBot
    id_chat = chat_id
    url = f"https://api.telegram.org/bot{token_bot}/sendDocument"
    with open(archivo,'rb') as documento:
        peticion = requests.post(url, files={"document": documento}, data={
                                'chat_id': id_chat, "caption": f"{info_msg}"})
        print(peticion)
