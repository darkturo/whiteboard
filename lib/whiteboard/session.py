import hashlib
import random
import time

from flask import request


def gen_session():
    salt = random.getrandbits(128)
    current_time = time.time()
    user_agent = request.headers.get('User-Agent')

    text = "<{ua}|{time}|{salt}>".format(ua=user_agent, time=current_time, salt=salt)

    return hashlib.sha512(text).hexdigest()[:16]
