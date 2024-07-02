def ButtonsMessage(number):
    data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {
                    "text": "¿Por donde quieres empezar?"
                },
                "action": {
                    "buttons": [
                        {
                            "type": "reply",
                            "reply": {
                                "id": "button_Explorar",
                                "title": "Explorar planes ✈️"
                            }
                        },
                        {
                            "type": "reply",
                            "reply": {
                                "id": "button_Preguntar",
                                "title": "Hacer una pregunta 🤖"
                            }
                        }
                    ]
                }
            }
        }
    
    return data

def ButtonsMessageSeguirExplorando(number):
    data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {
                    "text": "¿Te gustaría seguir explorando?"
                },
                "action": {
                    "buttons": [
                        {
                            "type": "reply",
                            "reply": {
                                "id": "button_si",
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