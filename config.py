import os
from dotenv import load_dotenv

load_dotenv()


config = {
            'server':           '2captcha.com',
            'apiKey':           os.getenv("API_KEY"),
            'defaultTimeout':    120,
            'recaptchaTimeout':  600,
            'pollingInterval':   10,
        }