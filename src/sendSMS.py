import os

import africastalking
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Africa's Talking
api_key = os.getenv('AT_API_KEY')
username = os.getenv('AT_USERNAME')
short_code = os.getenv('AT_SHORT_CODE')

africastalking.initialize(username, api_key)
sms = africastalking.SMS


def send_sms(to_numbers, message):
    try:
        if to_numbers is not list:
            to_numbers = [to_numbers]
        response = sms.send(message, to_numbers, short_code)
        print(response)
    except Exception as e:
        print(f'Issue: {e}')
