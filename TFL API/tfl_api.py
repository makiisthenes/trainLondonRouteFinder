import requests
import os
import time
import colorama
from colorama import init
from colorama import Fore, Back, Style

tfl_api_id = '158d290e'
tfl_api_key = '6192c53aa8807df16ad4f00b76bf7b00'
#print(tfl1)

init()


while 1 != 0:
    tfl1 = requests.get('https://api.tfl.gov.uk/Line/Mode/tube/Status?detail=false&app_id=158d290e&app_key=6192c53aa8807df16ad4f00b76bf7b00').json()
    print(tfl1[0]['name']+ ' --> ' + tfl1[0]['lineStatuses'][0]['statusSeverityDescription'])
    print(tfl1[1]['name']+ ' --> ' + tfl1[1]['lineStatuses'][0]['statusSeverityDescription'])
    print(tfl1[2]['name']+ ' --> ' + tfl1[2]['lineStatuses'][0]['statusSeverityDescription'])
    print(tfl1[3]['name']+ ' --> ' + tfl1[3]['lineStatuses'][0]['statusSeverityDescription'])
    print(tfl1[4]['name']+ ' --> ' + tfl1[4]['lineStatuses'][0]['statusSeverityDescription'])
    print(tfl1[5]['name']+ ' --> ' + tfl1[5]['lineStatuses'][0]['statusSeverityDescription'])
    print(tfl1[6]['name']+ ' --> ' + tfl1[6]['lineStatuses'][0]['statusSeverityDescription'])
    print(tfl1[7]['name']+ ' --> ' + tfl1[7]['lineStatuses'][0]['statusSeverityDescription'])
    print(tfl1[8]['name']+ ' --> ' + tfl1[8]['lineStatuses'][0]['statusSeverityDescription'])
    print(tfl1[9]['name']+ ' --> ' + tfl1[9]['lineStatuses'][0]['statusSeverityDescription'])
    print(tfl1[10]['name']+ ' -->' + tfl1[10]['lineStatuses'][0]['statusSeverityDescription'])
    print('Bakerloo Line --> ' +tfl1[0]['lineStatuses'][0]['statusSeverityDescription'])
    time.sleep(10)
    os.system('cls')


