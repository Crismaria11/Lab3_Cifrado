"""
Laboratorio 3
Ejercicio 2

Extraído de: https://github.com/sqreen/DevelopersSecurityBestPractices/blob/master/_practices/timing-attack/_python/app.py

Este programa es el servidor que chequea si el token ingresado es igual al token secreto y en esta version es vulnerable al timing attack
"""

import time
from flask import Flask, request

app = Flask(__name__)

SECRET_TOKEN = 'sol'


def strcmp(s1, s2):
    if len(s1) != len(s2):
        return False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            return False
        time.sleep(0.01)
    return True


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
