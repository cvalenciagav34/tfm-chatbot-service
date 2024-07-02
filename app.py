from flask import  Flask, request
import util
import whatsappservice
import chatgptservice
import opcionesGenerales
import opcionesPlan

app = Flask(__name__)

#http://127.0.0.1:8000

@app.route('/welcome', methods=['GET'])
def index():
    return "welcome developer"

@app.route('/whatsapp', methods=['GET'])
def verifyToken():
    try:
        accessToken = "EAAPZCJ4vaPW0BO1XYSMXMNQKlCbEm1WZCOOhZCZBRxLhclP9UAZBcIKxyXQpezk4NhnQwxNpPiOfOBGzF4ilcA4MZCyf3pV8fqIg7ZA4SzZAmato3RjIRCzbfEJQWfyOZCSGZCv5gB4S4LXKRqjcuke8KNUHZAhIoP63AjyZAQL54T0dXYpvfeUiE3mb2PPPmhPA9igHF4bgG3Dz581larYd"
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if token != None and challenge != None and token == accessToken:
            return challenge
        else:
            return "", 400
    except:
        return "", 400

@app.route('/whatsapp', methods=['POST'])
def recievedMessage():
    try:
        body = request.get_json()
        entry = (body["entry"])[0]
        changes = (entry["changes"])[0]
        value = changes["value"]
        message = (value["messages"])[0]
        number = message["from"]
        
        text = util.getTextUser(message)
        processMessage(text, number)
        # 
        # print (text)

        return "EVENT RECEIVED"
    except:
        return "EVENT RECEIVED"

def processMessage(text, number):
    text = text.lower()
    listData = []
    try:
        if "hola" in text:
            data = util.textMessage("Hola, te damos la bienvenida a la IA Turismo MED", number)
            dataMenu = opcionesGenerales.ButtonsMessage(number)
            listData.append(data)
            listData.append(dataMenu)   
        elif "explorar planes" in text:
            data = util.textMessage("¿Qué te gustaría hacer?", number)
            dataMenu = opcionesPlan.ListsMessageIntereses(number)
            listData.append(data)
            listData.append(dataMenu)
        elif "historia medellín" in text:
            data = util.textMessage("¿Qué presupuesto tienes por día?", number)
            dataMenu = opcionesPlan.ListsMessagePresupuestoHistoria(number)
            listData.append(data)
            listData.append(dataMenu)
        elif "10.000 a 30.000"  in text:
            prompt = "Dame una sugerencia de dos tours para conocer la historia de Medellín donde su costo esté entre 10.000 a 30.000. Incluyendo el de la comuna 13. Inicia la respuesta desde las palabras te recomendaría."
            data = preguntarChatGPT(prompt,number)
            dataMenu = opcionesGenerales.ButtonsMessageSeguirExplorando(number)
            listData.append(data)
            listData.append(dataMenu)   
        elif "30.000 a 60.000"  in text:
            prompt = "Dame una sugerencia de dos sitios para conocer la historia de Medellín donde su costo esté entre 30.000 a 60.000. Inicia la respuesta desde las palabras te recomendaría."
            data = preguntarChatGPT(prompt,number)
            dataMenu = opcionesGenerales.ButtonsMessageSeguirExplorando(number)
            listData.append(data)  
            listData.append(dataMenu) 
        elif "mayor a 60.000"  in text:
            prompt = "Dame una sugerencia de un tour bastante reconocidad para conocer Medellín y sus alrededores. Inicia la respuesta desde las palabras te recomendaría."
            data = preguntarChatGPT(prompt,number)
            dataMenu = opcionesGenerales.ButtonsMessageSeguirExplorando(number)
            listData.append(data) 
            listData.append(dataMenu) 
        elif "parches en medellín" in text:
            data = util.textMessage("¿Qué presupuesto tienes por día?", number)
            dataMenu = opcionesPlan.ListsMessagePresupuestoParches(number)
            listData.append(data)
            listData.append(dataMenu)
        elif "menos de 40.000"  in text:
            prompt = "Dame una sugerencia de dos lugares recomendados de la ciudad de Medellín para salir con amigos a comer o bailar y que no implique gastar más de 40.000. Inicia la respuesta desde las palabras te recomendaría."
            data = preguntarChatGPT(prompt,number)
            dataMenu = opcionesGenerales.ButtonsMessageSeguirExplorando(number)
            listData.append(data)
            listData.append(dataMenu)
        elif "40.000 a 80.000"  in text:
            prompt = "Dame una sugerencia de dos lugares recomendados de la ciudad de Medellín que tengan buen prestigio para salir con amigos a comer o bailar y que el valor oscile entre 40.000 a 80.000. Inicia la respuesta desde las palabras te recomendaría."
            data = preguntarChatGPT(prompt,number)
            dataMenu = opcionesGenerales.ButtonsMessageSeguirExplorando(number)
            listData.append(data)
            listData.append(dataMenu)
        elif "mayor a 80.000"  in text:
            prompt = "Dame una sugerencia de dos lugares recomendados de la ciudad de Medellín de muy alto prestigio para salir con amigos a comer o bailar y que el valor sea mayor a 80.000. Inicia la respuesta desde las palabras te recomendaría."
            data = preguntarChatGPT(prompt,number)
            dataMenu = opcionesGenerales.ButtonsMessageSeguirExplorando(number)
            listData.append(data)
            listData.append(dataMenu) 
        elif "si" in text:
            data = util.textMessage("¿Qué te gustaría hacer?", number)
            dataMenu = opcionesPlan.ListsMessageIntereses(number)
            listData.append(data)
            listData.append(dataMenu) 
        elif "no" in text and len(text) <=2:
            data = preguntarChatGPT("Quiero cerrar este chat. Inicia tu respuesta con 'Es un gusto ayudarte' y no hagas preguntas.",number)
            listData.append(data) 
        else:
            data = preguntarChatGPT(text,number)
            listData.append(data)        

        for item in listData:
            whatsappservice.sendMessageWhatsapp(item)
    except Exception as exception:
        print(exception)
        
def preguntarChatGPT(text, number):
    responseGPT = chatgptservice.getResponse(text)
    if responseGPT != "error":
        data = util.textMessage(responseGPT, number)
    else:
        data = util.textMessage("Lo siento ocurrió un problema", number)
    return data

def generateMessage(text, number):

    text = text.lower()
    if "text" in text:
        data = util.textMessage("Text", number)
    if "format" in text:
        data = util.textFormatMessage(number)
    if "image" in text:
        data = util.ImageMessage(number)
    if "video" in text:
        data = util.VideoMessage(number)
    if "audio" in text:
        data = util.AudioMessage(number)
    if "document" in text:
        data = util.DocumentMessage(number)
    if "button" in text:
        data = util.ButtonsMessage(number)
    if "list" in text:
        data = util.ListsMessage(number)
    if "location" in text:
        data = util.LocationMessage(number)

    whatsappservice.sendMessageWhatsapp(data)

if(__name__ == '__main__'):
    app.run(port=8000, debug=True)