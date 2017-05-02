#!/usr/bin/env python

import os
import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def default():
    return 'Hello, world!'

@app.route('/sleep/<seconds>')
def sleep(seconds):
    time.sleep(int(seconds))
    return 'I slept for {} seconds.'.format(seconds)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', '8080')), debug=True)
