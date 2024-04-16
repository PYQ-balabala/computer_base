def print_info(first_name, last_name, **kwargs):
    print(f'hello {first_name} {last_name}')
    for k, v in kwargs.items():
        print(f'{k}, {v}')
print_info('Tony', 'christo', dev='computer', favrite='bool')