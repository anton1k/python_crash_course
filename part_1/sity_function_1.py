def get_formatted_sity(sity, country, population = ''):
    '''Строит отформатированное город страна'''

    if population:
        full_sity = sity.title() + ', ' + country.title() + ' - численность ' + str(population)
    else:
        full_sity = sity.title() + ', ' + country.title()
        
    return full_sity
