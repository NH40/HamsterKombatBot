import json
import random
import string
import base64
import hashlib


def generate_random_visitor_id():
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    visitor_id = hashlib.md5(random_string.encode()).hexdigest()

    return visitor_id


def escape_html(text: str) -> str:
    return text.replace('<', '\\<').replace('>', '\\>')


def decode_cipher(cipher: str) -> str:
    encoded = cipher[:3] + cipher[4:]
    return base64.b64decode(encoded).decode('utf-8')


def get_headers(name: str):
    try:
        with open('profile.json', 'r') as file:
            profile = json.load(file)
    except:
        profile = {}

    headers = profile.get(name, {}).get('headers', {})

    return headers


def get_fingerprint(name: str):
    try:
        with open('profile.json', 'r') as file:
            profile = json.load(file)
    except:
        profile = {}

    fingerprint = profile.get(name, {}).get('fingerprint', {})

    fingerprint['visitorId'] = generate_random_visitor_id()

    return fingerprint
