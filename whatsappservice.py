import requests
import json

def sendMessageWhatsapp(data):
    try:
        token = "EAAPZCJ4vaPW0BOZCwIHkpYDw3VU32atnbkCEf710PKupNyNAsZBxDH0MZAdvZAZB63rBV7srFfevVacv7En1lUEoauVJtjpcfly8EcAk358fIDRH7sqSnXTIyHZBID9y0ZBVj5ANuIOQsuZBvdahzbIR9ZAmB6aEXxGZAsZCOfqJGtBmrfZATdQU830L2N8hMMlyGZBG5vNq8nRM8lTsr1dOfh"
        api_url = "https://graph.facebook.com/v19.0/359237617272485/messages"
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        response = requests.post(api_url, data = json.dumps(data), headers = headers)

        if response.status_code == 200:
            return True
        return False
    except Exception as exception:
        print(exception)
        return False