# Pharma WhatsApp Bot

A Python learning prototype for answering routine pharmacy inquiries through a Twilio-compatible WhatsApp webhook.

## Purpose

Explore how a conversational menu can help customers find common information before contacting staff.

## Implemented features

- Numbered menu for location, opening hours, insurance providers, delivery and requests for human assistance.
- Keyword matching for frequently asked questions, with a main-menu fallback.
- FastAPI `GET /` status endpoint.
- FastAPI `POST /webhook` endpoint: reads the `Body` form field and returns TwiML XML.

## Technology and files

Python, FastAPI and Twilio.

| File | Purpose |
| --- | --- |
| `main.py` | Reply content, matching rules and HTTP endpoints |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Local files excluded from version control |

## Current scope

This is a prototype, not a production support platform. Replies are fixed strings, not AI-generated answers. Stock, prices and insurance eligibility are not connected to live systems. The human-assistance option returns a message only; it does not notify or transfer to an operator.

For experimentation, use synthetic messages: the current implementation prints incoming messages to application logs. Webhook signature validation and a real operator notification flow are still needed before production use. Review the pharmacy-specific information in the source before reusing it.

## En español

Prototipo de atención por WhatsApp que responde consultas frecuentes de farmacia mediante un menú y palabras clave. Desarrollado con Python, FastAPI y Twilio.

El proyecto explora la atención de consultas habituales: ubicación, horarios, obras sociales y delivery. No consulta stock o precios reales ni deriva conversaciones a un operador; esas integraciones están pendientes.
