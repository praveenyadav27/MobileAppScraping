import requests as r
import pandas as pd
import csv
import xmltodict


fl = pd.read_csv(r'C:\Users\HP\Downloads\clubfftt.csv')
key_list = fl.club_numero.to_list()
headers = {'user-agent': 'UnityPlayer/2019.4.15f1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)'}
final_data_list = []
try:
    def scraping():
        """"""
        for key in key_list:
            make_url = 'https://fftt.dafunker.com//v1/proxy/xml_club_detail.php?club='+str(key)
            print(make_url)
            data_source = r.get(make_url, headers=headers, verify=False)
            data_dict = xmltodict.parse(data_source.text)
            data_club = data_dict['liste']['club']
            final_dict = {
                'idclub ': data_club['idclub'],
                'nom ': data_club['nom'],
                'nomsalle ': data_club['nomsalle'],
                'adressesalle1 ': data_club['adressesalle1'],
                'adressesalle2 ': data_club['adressesalle2'],
                'adressesalle3 ': data_club['adressesalle3'],
                'codepsalle ': data_club['codepsalle'],
                'villesalle ': data_club['villesalle'],
                'web ': data_club['web'],
                'nomcor ': data_club['nomcor'],
                'prenomcor ': data_club['prenomcor'],
                'mailcor ': data_club['mailcor'],
                'telcor ': data_club['telcor'],
                'latitude ': data_club['latitude'],
                'longitude ': data_club['longitude'],
                'datevalidation ': data_club['datevalidation']
                }
            final_data_list.append(final_dict)
            with open('ftte_data.csv', 'w', encoding='utf-8 + sig', newline='') as f:
                w = csv.writer(f)
                w.writerow(['idclub',
                            'nom',
                            'nomsalle',
                            'adressesalle1',
                            'adressesalle2',
                            'adressesalle3',
                            'codepsalle',
                            'villesalle',
                            'web',
                            'nomcor',
                            'prenomcor',
                            'mailcor',
                            'telcor ',
                            'latitude',
                            'longitude',
                            'datevalidation'])
                for fdl in final_data_list:
                    w.writerow(fdl.values())
except Exception as ex:
    print('Please check input or contact support!' + ' Hint: ' + str(ex))

if __name__ == "__main__":
    scraping()



