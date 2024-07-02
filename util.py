def getTextUser(message):
    text = ""
    typeMessage = message["type"]

    if typeMessage == "text":
        text = (message["text"])["body"]
    elif typeMessage == "interactive":
        interactiveObject = message["interactive"]
        typeInteractive = interactiveObject["type"]
        if typeInteractive == "button_reply":
            text = (interactiveObject["button_reply"])["title"]
        elif typeInteractive == "list_reply":
            text = (interactiveObject["list_reply"])["title"]
        else:
            print("sin mensaje")
    else:
        print ("sin mensaje")
    
    return text

def textMessage(text, number):
    data = {
                "messaging_product": "whatsapp",    
                "recipient_type": "individual",
                "to": number,
                "type": "text",
                "text": {
                    "body": text
                }
            }
    return data

def textFormatMessage(number):
    data = {
                "messaging_product": "whatsapp",    
                "recipient_type": "individual",
                "to": number,
                "type": "text",
                "text": {
                    "body": "*Información Importante*\n_Necesitas enviar tu correo_\n-Pero tiene que estar en-\n```en diferente formato```"
                }
            }
    return data

def ImageMessage(number):
    data = {
                "messaging_product": "whatsapp",    
                "recipient_type": "individual",
                "to": number,
                "type": "image",
                "image": {
                    "link": "https://res.cloudinary.com/worldpackers/image/upload/c_fill,f_auto,q_auto,w_1024/v1/guides/article_cover/jdkvvedeqvyrkltcny1z"
                }
            }
    return data

def AudioMessage(number):
    data = {
                "messaging_product": "whatsapp",    
                "recipient_type": "individual",
                "to": number,
                "type": "audio",
                "audio": {
                    "link": "https://music.apple.com/es/album/colombianos-comuna-13/1435690899?i=1435691055"
                }
            }
    return data

#para que funcione debe alojarse en la nube con la extensión
def VideoMessage(number):
    data = {
                "messaging_product": "whatsapp",    
                "recipient_type": "individual",
                "to": number,
                "type": "video",
                "audio": {
                    "link": "https://www.youtube.com/watch?v=St9kxRrx2mk"
                }
            }
    return data

#para que funcione debe alojarse en la nube con la extensión
def DocumentMessage(number):
    data = {
                "messaging_product": "whatsapp",    
                "recipient_type": "individual",
                "to": number,
                "type": "document",
                "document": {
                    "link": "https://drive.google.com/file/d/1003l625HecP4ZowwVj9Eg-ffzw6xgYP5/view?usp=sharing"
                }
            }
    return data

def LocationMessage(number):
    data = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": number,
                "type": "location",
                "location": {
                    "latitude": "6.256719279262453",
                    "longitude": "-75.62135882252012",
                    "name": "Comuna 13 Medellín - desde python",
                    "address": "Comuna n.º 13 San Javier"
                }
            }
    return data

def ButtonsMessage(number):
    data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {
                    "text": "¿Quieres cerrar el chat?"
                },
                "action": {
                    "buttons": [
                        {
                            "type": "reply",
                            "reply": {
                                "id": "button_yes",
                                "title": "Si"
                            }
                        },
                        {
                            "type": "reply",
                            "reply": {
                                "id": "button_no",
                                "title": "No"
                            }
                        }
                    ]
                }
            }
        }
    
    return data

def ListsMessage(number):
    data = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": number,
                "context": {
                    "message_id": "Cuéntanos que te gustaría conocer"
                },
                "type": "interactive",
                "interactive": {
                    "type": "list",
                    "body": {
                        "text": "✅ Tenemos estas opciones"
                    },
                    "footer": {
                        "text": "Selecciona una opción"
                    },
                    "action": {
                        "button": "Ver opciones",
                        "sections": [
                            {
                                "title": "Restaurantes",
                                "rows": [
                                    {
                                        "id": "rest_1",
                                        "title": "Doña Panchita",
                                        "description": "Restaurante doña Panchita"
                                    },
                                    {
                                        "id": "rest_2",
                                        "title": "Empanadas siempre listas",
                                        "description": "Empandas siempre listas"
                                    }
                                ]
                            },
                            {
                                "title": "Lugares típicos",
                                "rows": [
                                    {
                                        "id": "lugar_1",
                                        "title": "Comuna 13",
                                        "description": "Comuna 13 Medellín"
                                    },
                                    {
                                        "id": "lugar_2",
                                        "title": "Hacienda",
                                        "description": "Hacienda de Pablo Escobar"
                                    }
                                ]
                            }
                        ]
                    }
                }
            }
    
    return data