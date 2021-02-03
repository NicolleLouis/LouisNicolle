class UtilsService:
    @staticmethod
    def generate_french_postal_code():
        department_numbers = range(96)
        return list(
            map(
                UtilsService.generate_french_postal_code_callback,
                department_numbers
            )
        )

    @staticmethod
    def generate_french_postal_code_callback(number):
        if number == 75:
            return "75001"
        elif number == 13:
            return "13001"
        elif number == 69:
            return "69001"
        elif number < 10:
            return '{}0000'.format(number)
        else:
            return '{}000'.format(number)
