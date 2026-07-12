from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from twilio.twiml.messaging_response import MessagingResponse

app = FastAPI()

DIRECCION = "Av. Rivadavia 11552, Liniers, CABA."

HORARIOS = (
    "Nuestro horario de atencion es:\n"
    "Lunes a viernes de 8:00 a 21:00hs.\n"
    "Sabados, domingos y feriados de 10:00 a 20:00hs."
)

OBRAS_SOCIALES = (
    "Trabajamos con: ObsBA, Swiss Medical, Omint, Union Personal "
    "(excepto plan diabetes y monotributo), Avalian, Sanidad, Galeno, "
    "DAS Congreso, Poder Judicial, entre otras. Decime la tuya y te confirmo la cobertura."
)

DELIVERY = "Por el momento el servicio de delivery esta suspendido. Podes acercarte en nuestro horario de atencion."

ESCALACION_MENSAJE = (
    "Entendido. En breve una persona del equipo se va a contactar con vos "
    "para ayudarte. Gracias por tu paciencia."
)

MENU = (
    "Hola! Te comunicaste con Farmacia SER, elegi una opción escribiendo el número:\n\n"
    "1 - Donde estamos ubicados\n"
    "2 - Horarios de atencion\n"
    "3 - Obras sociales y prepagas\n"
    "4 - Delivery\n"
    "5 - Hablar con alguien del equipo"
)

OPCIONES_MENU = {
    "1": DIRECCION,
    "2": HORARIOS,
    "3": OBRAS_SOCIALES,
    "4": DELIVERY,
    "5": ESCALACION_MENSAJE,
}

PALABRAS_ESCALACION = [
    "hablar con alguien", "hablar con una persona", "hablar con el farmaceutico",
    "operador", "atencion humana", "persona real", "humano", "encargado",
]

FAQS = {
    "horario": HORARIOS,
    "direccion": DIRECCION,
    "ubicacion": DIRECCION,
    "donde estan": DIRECCION,
    "delivery": DELIVERY,
    "envio": DELIVERY,
    "receta": "Para medicamentos que requieren receta, podes enviarnos una foto clara de la misma por aca.",
    "obra social": OBRAS_SOCIALES,
    "prepaga": OBRAS_SOCIALES,
    "turno": "No trabajamos con sistema de turnos, podes acercarte en nuestro horario de atencion.",
    "precio": "Decime el nombre del producto y te paso el precio actualizado.",
    "stock": "Decime el nombre del producto y te confirmo si tenemos stock disponible.",
    "vacuna": "Si, aplicamos vacunas. Contanos cual necesitas para darte mas informacion.",
    "farmaceutico": "Nuestro farmaceutico esta disponible en el horario de atencion para consultas.",
}


def buscar_respuesta(mensaje: str) -> str:
    mensaje_limpio = mensaje.strip().lower()

    if mensaje_limpio in OPCIONES_MENU:
        return OPCIONES_MENU[mensaje_limpio]

    for frase in PALABRAS_ESCALACION:
        if frase in mensaje_limpio:
            return ESCALACION_MENSAJE

    for palabra_clave, respuesta in FAQS.items():
        if palabra_clave in mensaje_limpio:
            return respuesta

    return MENU


@app.get("/")
async def root():
    return {"status": "Pharma Bot WhatsApp - activo"}


@app.post("/webhook")
async def whatsapp_webhook(request: Request):
    form_data = await request.form()
    mensaje_recibido = form_data.get("Body", "")
    numero_remitente = form_data.get("From", "")

    print(f"Mensaje de {numero_remitente}: {mensaje_recibido}")

    respuesta_texto = buscar_respuesta(mensaje_recibido)

    respuesta_twiml = MessagingResponse()
    respuesta_twiml.message(respuesta_texto)

    return PlainTextResponse(content=str(respuesta_twiml), media_type="application/xml")