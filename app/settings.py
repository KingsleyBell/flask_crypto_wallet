import os

WALLET_USERNAME = os.environ.get('WALLET_USERNAME', default='user')
WALLET_PASSWORD = os.environ.get('WALLET_PASSWORD', default='password')
INPUT_FILE_PATH = os.environ.get('INPUT_FILE_PATH', default='tick.log')
