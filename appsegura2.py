"""
Laboratorio 3
Ejercicio 2

Extraído de: https://github.com/sqreen/DevelopersSecurityBestPractices/blob/master/_practices/timing-attack/_python/app.py

Este programa es el servidor que chequea si el token ingresado es igual al token secreto y en esta version es seguro usando la segunda solución
donde se pasa cada token por HMAC.
"""

import time
from flask import Flask, request
import hmac

app = Flask(__name__)

SECRET_TOKEN = 'sol'


def strcmp(s1, s2):
    if len(s1) != len(s2):
        return False

    key = b"123"
    hmac1 = hmac.new(key, msg=s1.encode(), digestmod="sha256")
    hmac2 = hmac.new(key, msg=s2.encode(), digestmod="sha256")
    return hmac1.digest() == hmac2.digest()


@app.route("/")
def protected():
    token = request.headers.get('X-TOKEN')

    if not token:
        return "Missing token", 401

    if strcmp(token, SECRET_TOKEN):
        return "Hello admin user! Here is your secret content"
    else:
        return "WHO ARE YOU? GET OUT!", 403


if __name__ == "__main__":
    app.run()
