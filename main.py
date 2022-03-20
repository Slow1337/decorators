import time
import requests

def logging_decorator(some_basic_func, path='log.txt'):
    log_dict = {
        'timedate': None,
        'pos_arguments': None,
        'kw_args': None,
        'return': None
    }
    def new_function(*args, **kwargs):
        log_dict['timedate'] = time.asctime()
        log_dict['pos_arguments'] = args
        log_dict['kw_args'] = kwargs
        log_dict['return'] = some_basic_func(*args, **kwargs)
        with open(path, 'w', encoding='utf-8', ) as logfile:
            for key in log_dict:
                data = log_dict[key]
                logfile.write(f'{key}: {data}\n')
        return some_basic_func(*args, **kwargs)
    print('log is written')
    return new_function

@logging_decorator
def get_hero_int(*args):
    hero_list = args
    access_token = 2619421814940190
    hero_int = {}
    for name in hero_list:
        url = f'https://superheroapi.com/api/{access_token}/search/{name}'
        response = requests.get(url)
        response = response.json()
        intelligence = response['results'][0]['powerstats']['intelligence']
        hero_int.update({intelligence: name})
    smartest_hero = max(hero_int.keys())
    smartest_hero = hero_int[smartest_hero]
    return smartest_hero

get_hero_int('Thor', 'Hulk', 'Captain America')
