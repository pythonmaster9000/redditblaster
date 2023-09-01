import json
import random


def get_random_proxy():
    with open("proxies.json", 'r') as f:
        proxs = json.load(f)
    if len(proxs['proxies']) == 0:
        return None
    return random.choice(proxs['proxies'])