import requests
from dotenv import load_dotenv
import os
import json

def sendMessageWhatsapp(data):
    try:
        # Leer el archivo de configuración
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
        token_json = config.get('token_whatsapp')
        load_dotenv()
        token = os.getenv('token_whatsapp',token_json)
        api_url = "https://graph.facebook.com/v19.0/359237617272485/messages"
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        response = requests.post(api_url, data = json.dumps(data), headers = headers)

        if response.status_code == 200:
            return True
        return False
    except Exception as exception:
        print(exception)
        return False