import sys
sys.path.insert(0, './json/')
import json
import pygal
from country_codes import get_country_code

# список заполняется данными
filename = 'gdp_json.json'
with open(filename) as f:
    pop_data = json.load(f)

# Вывод ВВП каждой страны за 2010 год.
cc_vvp = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == 2010:
        country_name = pop_dict['Country Name']
        vvp = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_vvp[code] = vvp

cc_pop_1, cc_pop_2, cc_pop_3 = {}, {}, {}
for cc, pop in cc_vvp.items():
    if pop < 10000000:
        cc_pop_1[cc] = pop
    elif pop < 1000000000:
        cc_pop_2[cc] = pop
    else:
        cc_pop_3[cc] = pop

wm = pygal.maps.world.World()
wm.title = 'World ВВП in 2010, by Country'
wm.add('0-10m', cc_pop_1)
wm.add('10m-1bn', cc_pop_2)
wm.add('>1bn', cc_pop_3)

wm.render_to_file('world_vvp.svg')