#!/usr/bin/env python

import os
import requests

host = os.getenv('SLEEP_HOST', 'localhost:8080')
requests.get('http://{}/'.format(host))
sleep_time = 330
print '{}-second request starting...'.format(sleep_time)
response = requests.get('http://{}/sleep/{}'.format(host, sleep_time))
response.raise_for_status()
print '{}-second request done.'.format(sleep_time)
# while True:
#     print '{}-second request starting...'.format(sleep_time)
#     response = requests.get('http://{}/sleep/{}'.format(host, sleep_time))
#     response.raise_for_status()
#     print '{}-second request done.'.format(sleep_time)
#     sleep_time *= 2
