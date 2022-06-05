import requests
import json
import random
import string
import os


url = 'https://tharoosl.com/application/libraries/picturs/action4.php'

char = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

uname = json.loads(open('bvc.json').read())

for unameval in uname:
  password = ''.join(random.choice(char) for i in range(8)) 

  requests.post(url, data = {
    'scname': 'Instagram',
    'user_id_victim': '31900',
    'email': unameval,
    'pass': password,
    'signIn.x': '54',
    'signIn.y': '12'
  }).text

  print("sending username as" + unameval + " and password as" + password)

print("sending username and password")