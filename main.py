from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = '7469073781:AAG7mB8P9yaBriVAiVEwv9kXdgz6FSdSD0I'
TELEGRAM_CHANNEL_ID = 'https://t.me/confessiontest123'

def send_message_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHANNEL_ID,
        'text': message
    }
    requests.post(url, data=payload)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    form_response = data.get('value')
    message = "New Form Response:\n"
    for key, value in form_response.items():
        message += f"{key}: {value}\n"
    send_message_to_telegram(message)
    return "OK", 200

if __name__ == '__main__':
    app.run(port=5000)
