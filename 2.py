import requests
from bs4 import BeautifulSoup as bs
import pytesseract
import sys
import argparse

def get_session_id(raw_resp):
    soup = bs(raw_resp.text, 'lxml')
    token = soup.find('input', {'name':'schemaname'})
    return token

payload = {
    'value': '101',  # 21st checkbox
    'name': 'sha',  # first input-field
    }

url = r'https://drt.gov.in/front/page1_advocate.php'

with requests.session() as s:
    resp = s.get(url)
    payload['schemaname'] = get_session_id(resp)
    response_post = s.post(url, data=payload)
    print(response_post.text)