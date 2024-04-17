def get_full_name(first_name, last_name, **kwargs):
    full_name = first_name + ' ' + last_name
    return full_name.title()


get_full_name('Tony', 'christo', dev='computer', favrite='bool')
