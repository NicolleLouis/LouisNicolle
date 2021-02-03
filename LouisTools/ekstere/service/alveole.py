class AlveoleService:
    @staticmethod
    def clean_raw_json(raw_json):
        internet_adress = raw_json["website"] if "website" in raw_json else "Non renseigné"
        site_type = "Réparateur" if raw_json["gender"] == 0 else "Ateliers associatifs"

        return {
            "nom": raw_json["commercialname"],
            "adresse": raw_json["adresse"],
            "code_postal": raw_json["zip"],
            "ville": raw_json["city"],
            "telephone": raw_json["telephone"],
            "internet": internet_adress,
            "type": site_type,
        }
