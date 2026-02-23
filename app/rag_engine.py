# backend/app/rag_engine.py
import openai
from .config import OPENAI_API_KEY, MODEL_NAME

openai.api_key = OPENAI_API_KEY

def generate_answer(query, context_chunks):
    context_text = "\n\n".join([f"File: {c['file_name']}\n{c['text']}" for c in context_chunks])
    
    prompt = f"Use this code context to answer: {context_text}\n\nQuestion: {query}"

    try:
        # Ikkada spacing (Indentation) chala important
        response = openai.ChatCompletion.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        # Ikkada kuda space undali
        return f"OpenAI Error: {str(e)}"