import requests
import json

from django.core.management.base import BaseCommand

from ekstere.constants.alveole import url_coupdepoucevelo, url_data_gouv
from ekstere.service.utils import UtilsService
from ekstere.service.alveole import AlveoleService


class Command(BaseCommand):
    help = 'Scrap Alveole website'

    def handle(self, *args, **options):
        ateliers = []
        postal_codes = UtilsService.generate_french_postal_code()
        for postal_code in postal_codes:
            request_gouv = requests.get(url_data_gouv.format(postcode=postal_code))
            features = request_gouv.json()['features']
            if len(features) > 0:
                coordinates = request_gouv.json()['features'][0]['geometry']["coordinates"]
                longitude = coordinates[0]
                latitude = coordinates[1]
                request_coupdepouce = requests.get(
                    url_coupdepoucevelo.format(
                        latitude=latitude,
                        longitude=longitude
                    )
                )
                ateliers.append(
                    list(
                        map(
                            AlveoleService.clean_raw_json,
                            request_coupdepouce.json()
                        )
                    )
                )
            else:
                print("Il y a eu une couille ici: {}".format(postal_code))
        with open('result.txt', 'w') as f:
            json.dump(ateliers, f, ensure_ascii=False)
