#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

site="http://..."
for alankodu in [537, 538, 539]:
    for telno in range(0, 9999999):
        telefon=str(alankodu) +'{:07}'.format(telno)
        req = requests.post(site,
                            data={'phone_number': telefon, 'submit': 'Engelle'})
        soup = BeautifulSoup(req.text.encode('iso-8859-9').decode(), 'html.parser')
        mesaj = soup.select("div.alert")[0].get_text()
        print(mesaj)

