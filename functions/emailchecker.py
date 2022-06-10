import requests
import os
import random
import json

def isEmailFake(email):
    temp_mail = json.loads(open('utils/email.json').read())
    splitter = email.split("@")
    domain = splitter[1]
    for bogus_domain in temp_mail:
      if(domain == bogus_domain):
        return True
      else:
        return False

g