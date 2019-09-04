def get_formatted_sity(sity, country):
    '''Строит отформатированное город страна'''
    full_sity = sity + ', ' + country
    return full_sity.title()