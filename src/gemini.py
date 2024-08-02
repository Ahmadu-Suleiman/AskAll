import os
import textwrap

import google.generativeai as genai
import jsonpickle
from dotenv import load_dotenv
from google.generativeai.types import StopCandidateException

import firebase

load_dotenv()

# configure gemini
gemini_api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel('gemini-1.5-flash')
wrapper = textwrap.TextWrapper(width=50)


def get_response(prompt, number):
    try:
        history = firebase.get_member_history(number)
        if len(history) == 0:
            prompt = textwrap.dedent(f''' You are a knowledgeable agricultural expert chatbot designed to assist farmers 
            with their queries. Your target audience is small-scale farmers in rural areas with limited agricultural 
            knowledge. You are to recognize and respond in the same language their questions are asked (English, Hausa, 
            Yoruba, Pidgin). Respond in a friendly, informative, and helpful manner, using simple language. Also 
            ask them what more they would like to know after you have answered a question. Generate responses in less 
            than 400 character count. Here is their first question, "{prompt}".''')
            history = [{"role": "user", "parts": [{"text": prompt}]}]

        chat = model.start_chat(history=history)
        response = chat.send_message(prompt)
        history = jsonpickle.encode(chat.history, True)
        firebase.set_member_history(number=number, history=history)

        return wrapper.fill(response.text.replace('*', ''))
    except StopCandidateException:
        return 'Error, please ask another question'
