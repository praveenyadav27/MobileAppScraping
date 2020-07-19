#!/usr/bin/env python
# coding: utf-8

import requests
import json
import datetime
import csv
import time


url = 'https://ariadna.cuatroochenta.com/webservice.php/identification/'
post_data = r'{"username":"c.fernandez.gcg.ac@gmail.com","password":"e10adc3949ba59abbe56e057f20f883e"}'
headers = {
    'User-Agent':'okhttp/3.12.1',
    'Connection': 'Keep-Alive',
    'Content-Type': 'application/json'
    }
headers_new = {
    'User-Agent':'okhttp/3.12.1',
    'Connection': 'Keep-Alive',
    'Content-Type': 'application/json',
    'Accept-Encoding':'gzip',
    'auth-token':'33b13ce596acfa5226608b514419cc53'
    }
cookies_new = {'symfony':'h7sp0hhr6t5llf7qgn9hvfldk4'}
next_url = 'https://ariadna.cuatroochenta.com/webservice.php/dea/search/'

def start_crawling():
    """"function to scrape the mosque data from an app.
        Do not run it you donot need the data.""""
    try:
        res = requests.post(url, data = post_data, headers = headers , verify = False )
        datajson = json.loads(res.text)
        auth_token = datajson['auth_token']
        #print(auth_token)
        time.sleep(3)

        post_data_new = r'{"criteria":{"pageSize":2500,"excludeIds":[],"initialCoordinates":{"lat":17.4673609,"long":78.3548533},"boundingBox":{}}}'
        res_next = requests.post(next_url, data = post_data_new, headers = headers_new , cookies =cookies_new,verify = False )
        with open('ariadna.json','w') as cm:
            cm.write(res_next.text)
        final_data_list = []
        time.sleep(5)
        with open('ariadna.json','r') as cm:
            list_data = json.loads(cm.readline())
        for i in list_data:
            final_dict = {
                    'id': i['id'],
                    'user_id': i['user_id'],
                    'name': i['name'],
                    'place_type_id': i['place_type_id'],
                    'address': i['address'],
                    'location_latitude': i['location_latitude'],
                    'location_longitude': i['location_longitude'],
                    'is_validated':  i['is_validated'],
                    'images': [image['image'] for image in i['images']],
                    'details': i['details'],
                    'contact': i['contact']
                    }
            final_data_list.append(final_dict)
        filename = 'ariadna' + datetime.datetime.now().strftime('data-%Y%m%d%H%M.csv')    
        with open(filename,'w', encoding='utf-8 + sig', newline='') as f:
            w = csv.writer(f)
            w.writerow(['id','user_id','name','place_type_id','address','location_latitude','location_longitude', 'is_validated', 'images', 'details', 'contact'])
            for fdl in final_data_list:
                w.writerow(fdl.values())
    except Exception as e:
        print('Please check input or contact support!'+ ' Hint: ' + str(e) )

if __name__ == "__main__":
    start_crawling()



