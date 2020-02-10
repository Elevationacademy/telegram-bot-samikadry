import math
import requests
from flask import Flask, Response, request

app = Flask(__name__)


@app.route('/sanity')
def sanity():return "Server is running"


TOKEN = '1009210321:AAHcEKy48Ogh1xrXit4oJQzX8QO8BsmbkKM'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url=https://39d134da.ngrok.io/message'.format(TOKEN)
requests.get(TELEGRAM_INIT_WEBHOOK_URL)


def isPrime(num):
    if num > 1:
        for i in range(2, (num // 2)+1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


def isFactorial(num):
    fact = i = 1
    while i <= num:
        fact *= i
        i += 1
        if fact == num:
            message = f"{num} is a result of factorial operation"
            return True
    return False


@app.route('/message', methods=["POST"])
def handle_message():
    message = " "
    message_info = request.get_json()
    chat_id = message_info['message']['chat']['id']
    command = message_info['message']['text']
    res = command.split()
    try:
        num = int(res[1])
        if res[0] == "check":
            if isPrime(num):
                message = f"{num} is a prime number"
            else:
                message = f"{num} isn't a prime number"

        elif res[0] == "factorial":
            if isFactorial(num):
                message = f"{num} is a result of factorial operation"
            else:
                message = f"{num} isn't a result of factorial operation"

        elif res[0] == "palindrome":
            if str(num) == str(num)[::-1]:
                message = f"{num} is PALINDROME"
            else:
                message = f"{num} isn't PALINDROME"

        elif res[0] == "sqrt":
            root = math.sqrt(num)
            if int(root + 0.5) ** 2 == num:
                message = f"{num} have an integer square root"
            else:
                message = f"{num} haven't an integer square root"

        else:
            message = f"Invalid command {res[0]}!!\n"
    except:
        message = f"Invalid input, must be a number after the command.\n"
    finally:
        requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(TOKEN, chat_id, message))
        return Response("success")


if __name__ == '__main__':
    app.run(port=5002)
