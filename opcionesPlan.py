def ListsMessageIntereses(number):
    data = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": number,
                "context": {
                    "message_id": "busqueda_plan"
                },
                "type": "interactive",
                "interactive": {
                    "type": "list",
                    "body": {
                        "text": "✅ Tenemos estas opciones"
                    },
                    "action": {
                        "button": "Ver opciones",
                        "sections": [
                            {
                                "title": "Intereses",
                                "rows": [
                                    {
                                        "id": "sitio_1",
                                        "title": "Historia Medellín 🚇 🏞️",
                                        "description": "Conocer la historia y la transformación de Medellín"
                                    },
                                    {
                                        "id": "sitio_2",
                                        "title": "Parches en Medellín 💃🕺",
                                        "description": "Descubre que hay pa hacer en Medellín"
                                    }
                                ]
                            },
                            {
                                "title": "Hacer pregunta",
                                "rows": [
                                    {
                                        "id": "sitio_7",
                                        "title": "Hacer una pregunta 🤖",
                                        "description": "Préguntale al chatbot"
                                    }
                                ]
                            }                       
                        ]
                    }
                }
            }
    
    return data

def ListsMessagePresupuestoHistoria(number):
    data = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": number,
                "context": {
                    "message_id": "presupuesto"
                },
                "type": "interactive",
                "interactive": {
                    "type": "list",
                    "body": {
                        "text": "🤑 Tenemos estas opciones"
                    },
                    "action": {
                        "button": "Ver opciones",
                        "sections": [
                            {
                                "title": "Historia de Medellín 💰",
                                "rows": [
                                    {
                                        "id": "ppto_1",
                                        "title": "10.000 a 30.000",
                                        "description": "de 10.000 a 30.000 por día"
                                    },
                                    {
                                        "id": "ppto_2",
                                        "title": "30.000 a 60.000",
                                        "description": "de 30.000 a 60.000 por día"
                                    },
                                    {
                                        "id": "ppto_3",
                                        "title": "Mayor a 60.000",
                                        "description": "Mayor a 60.000 por día"
                                    }
                                ]
                            },
                            {
                                "title": "Hacer pregunta",
                                "rows": [
                                    {
                                        "id": "ppto_7",
                                        "title": "Hacer una pregunta 🤖",
                                        "description": "Préguntale al chatbot"
                                    }
                                ]
                            }                          
                        ]
                    }
                }
            }
    
    return data

def ListsMessagePresupuestoParches(number):
    data = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": number,
                "context": {
                    "message_id": "¿Qué presupuesto tienes?"
                },
                "type": "interactive",
                "interactive": {
                    "type": "list",
                    "body": {
                        "text": "✅ Tenemos estas opciones"
                    },
                    "action": {
                        "button": "Ver opciones",
                        "sections": [
                            {
                                "title": "Parches en Medellín 💰",
                                "rows": [
                                    {
                                        "id": "ppto_4",
                                        "title": "Menos de 40.000",
                                        "description": "Menos de 40.000 por día"
                                    },
                                    {
                                        "id": "ppto_5",
                                        "title": "40.000 a 80.000",
                                        "description": "de 40.000 a 80.000 por día"
                                    },
                                    {
                                        "id": "ppto_6",
                                        "title": "Mayor a 80.000",
                                        "description": "Mayor a 80.000 por día"
                                    }
                                ]
                            },
                            {
                                "title": "Hacer pregunta",
                                "rows": [
                                    {
                                        "id": "ppto_7",
                                        "title": "Hacer una pregunta 🤖",
                                        "description": "Préguntale al chatbot"
                                    }
                                ]
                            }                           
                        ]
                    }
                }
            }
    
    return data