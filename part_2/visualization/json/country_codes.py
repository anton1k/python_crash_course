from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    '''Возвращает для заданной страны ее код в Pygal, состоящий из двух букв'''
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        # если сторана не неайдена, вернуть None
    return None

