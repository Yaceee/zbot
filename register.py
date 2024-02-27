import requests
import time
import re
import random

from wsid import getWsid
from idGenerator import generateId

def checkValidRegister(res: str, user_mail: str):
    if(len(re.findall(user_mail, res)) == 4):
        return True
    return False

def register():
    wsid = getWsid()

    user1 = generateId()
    user2 = generateId()

    url_timer = 'https://www.weezevent.com/widget_billeterie.php?id_evenement=1098393&locale=fr-FR&o=0&code=64869&color_primary=0032FA'

    data_timer = {
    'current_step': 'tickets',
    'widgetState': 'CartState',
    'wsid': wsid,
    'seatsToken': '',
    'montantBilletInitial_0': '0',
    'id_code_cpt_0': '4067115',
    'quantite_initiale_min_4067115': '0',
    'quantite_initiale_4067115': '2',
    'chps_montant_0': '0',
    'cpt_chps_4067115': '0',
    'group_size_4067115': '1',
    'aff_ht': '0',
    'aff_comm': '0',
    'quantite_4067115': '2',
    'chps_montant_final': '0',
    'chps_spb_amount_total_ttc': '0',
    'chps_spb_count_charged_tickets': '0',
    'id_evenement': '1098393',
    'nbCodeUsed': '0',
    }

    requests.post(url_timer, data_timer)

    time.sleep(2 + random.random())


    url = "https://www.weezevent.com/widget_billeterie.php?id_evenement=1098393&locale=fr-FR&code=64869&color_primary=0032FA"

    form_data = {
    'current_url': 'https://www.weezevent.com/widget_billeterie.php?id_evenement=1098393&locale=fr-FR&o=0&code=64869&color_primary=0032FA#Billetterie',
    'current_step': 'form',
    'widgetState': 'FormState',
    'wsid': wsid,
    'recapTickets': '[{"id":4067115,"name":"Billet - Meeting de lancement de campagne des Europ\u00e9ennes","quantity":"2"}]',
    'start_date': '0',
    'champs_3_4067115_1': user1[0],
    'champs_2_4067115_1': user1[1],
    'champs_1_4067115_1': 'M.',
    'champs_5_4067115_1': user1[5],
    'champs_6_4067115_1': user1[4],
    'champs_27_4067115_1': user1[3],
    'champs_28_4067115_1': 'Paris',
    'question_7532192_4067115_1': '',
    'champs_3_4067115_2': user2[0],
    'champs_2_4067115_2': user2[1],
    'champs_1_4067115_2': 'M.',
    'champs_5_4067115_2': user2[5],
    'champs_6_4067115_2': user2[4],
    'champs_27_4067115_2': user2[3],
    'champs_28_4067115_2': 'lol',
    'question_7532192_4067115_2': '',
    'champs_3_0': user1[0],
    'champs_2_0': user1[1],
    'champs_5_0': user1[5],
    'champs_36_0': user1[5],
    'champs_7_0': user1[4],
    'champs_27_0': user1[3],
    'champs_28_0': 'Paris',
    'champs_50_0': '0',
    'facturation': '0',
    'accepte_cgv': '1',
    'facturation_societe': '',
    'facturation_tva_intra': '',
    'facturation_adresse': '',
    'facturation_cp': '',
    'facturation_ville': '',
    'facturation_pays': '',
    'facturation_info': ''
    }

    res = requests.post(url, data=form_data)

    return checkValidRegister(res.text, user1[5])

if __name__ == '__main__':    
    print(register())
