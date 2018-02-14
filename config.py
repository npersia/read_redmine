import os

import pip

def install(package):
    pip.main(['install', package])

# Example
if __name__ == '__main__':
    install('requests')


workers = int(os.environ.get('GUNICORN_PROCESSES', '3'))
threads = int(os.environ.get('GUNICORN_THREADS', '1'))

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }
