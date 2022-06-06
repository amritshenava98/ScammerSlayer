import requests
import os
import random
import string
import json


def getRequestURL(url):
    request_url = url
    return request_url

def readDataSetValues(file_json):
    value = json.loads(open(file_json).read())
    return value

def generateCharacter():
    char = string.ascii_letters + string.digits  + '!@#$%^&*()'
    return char

def generatePassword(char):
    random.seed = (os.urandom(1024))
    password = ''.join(random.choice(char) for i in range(8))
    return password

def slayTarget(url, values):
    target = getRequestURL(url)
    values = readDataSetValues(values)
    char = generateCharacter()
    password = generatePassword(char)

    for value in values:

      requests.post(target, data = {
        'scname': 'Instagram',
        'user_id_victim': '31900',
        'email': value,
        'pass': password,
        'signIn.x': '54',
        'signIn.y': '12'
      }).text
      
      print("sending username as" + value + " and password as" + password)

    print("sending username and password")