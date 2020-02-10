import requests
from flask import Flask, Response, request
from DataBase import commands

app = Flask(__name__)


@app.route('/sanity')
def sanity():
    return "Server is running"


TOKEN = '1009210321:AAHcEKy48Ogh1xrXit4oJQzX8QO8BsmbkKM'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?' \
                            'url=https://39d134da.ngrok.io/message'.format(TOKEN)
requests.get(TELEGRAM_INIT_WEBHOOK_URL)


@app.route('/message', methods=["POST"])
def handle_message():
    message = " "
    message_info = request.get_json()
    chat_id = message_info['message']['chat']['id']
    command = message_info['message']['text']
    res = command.split()
    try:
        num = int(res[1])
        message = commands[res[0]](num)
    except:
        message = f"Invalid input!!\nthere are only 4 commands(check, factorial, palindrome, sqrt).\n" \
                  f"be sure to write a number after every command.\n"
    finally:
        requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(TOKEN, chat_id, message))
        return Response("success")


if __name__ == '__main__':
    app.run(port=5002)
