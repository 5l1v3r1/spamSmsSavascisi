#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

site="http://..."
postdata={'phone_number': telefon, 'submit': 'Engelle'}

for alankodu in [530, 532, 533, 534, 535, 536, 537, 538, 539, 505, 506, 507, 551, 552, 553, 554, 555, 556, 557, 558, 559,540, 541, 542, 543, 544, 545, 546, 547, 548, 549]:
    for telno in range(0, 9999999):
        telefon=str(alankodu) +'{:07}'.format(telno)
        req = requests.post(site, data=postdata)
        soup = BeautifulSoup(req.text.encode('iso-8859-9').decode(), 'html.parser')
        mesaj = soup.select("div.alert")[0].get_text()
        print(mesaj)
