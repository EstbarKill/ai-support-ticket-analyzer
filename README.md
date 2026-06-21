# AI Support Ticket Analyzer

Technical assessment for the AI Team.

## Stack

### Backend
- FastAPI
- SQLite
- SQLAlchemy

### AI
- Google Gemini
- Sentence Transformers

### RAG
- ChromaDB

### Frontend
- Next.js
- Tailwind CSS

## Status

🚧 Project initialization

## ¿Por qué no integraste Gemini primero?
Priorizé la construcción de una base de datos consistente y una capa de analítica antes de integrar IA. De esta manera pude validar la calidad de los datos, exponer métricas operativas y reutilizar la misma infraestructura tanto para el dashboard como para los procesos de enriquecimiento mediante LLM.

Cambiar el MOCK Provider

## ¿Por qué hacer esto antes de Gemini?
Diseñé una abstracción para el proveedor LLM. La aplicación funciona incluso sin API Key gracias a un Mock Provider, y cambiar a Gemini u OpenAI requiere únicamente implementar la misma interfaz.

La aplicación soporta múltiples proveedores LLM mediante una abstracción común. Actualmente implementé MockProvider y GeminiProvider, pero agregar OpenAI o Claude requeriría únicamente otra implementación de la interfaz.

Antes de entregrar hacer la migracion del gemini

import google.generativeai as genai <<x>> from google import genai
pip install google-genai

ash 
{
  "question": "What are the SLA rules?"
}