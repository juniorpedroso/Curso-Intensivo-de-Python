# try: pip3 install pygal.maps.world
# and then: from pygal.maps.world import COUNTRIES
# it does the same thing as i18n module

from pygal.maps.world import COUNTRIES

# for country_code in sorted(COUNTRIES.keys()):
#     print(country_code, COUNTRIES[country_code])


def get_country_code(country_name):
    """[Devolve o código de duas letras do Pygal para um país, 
    dado  o seu nome]"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

    # Se o país não foi encontrado, devolve None
    return None


