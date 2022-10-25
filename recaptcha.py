from twocaptcha import TwoCaptcha
from dotenv import load_dotenv
import os
from config import config

load_dotenv()


def get_recaptchaV2_token(sitekey, url):

    solver = TwoCaptcha(**config)

    result = solver.recaptcha(sitekey=sitekey,
                              url=url)

    return result['code']


print(get_recaptchaV2_token(sitekey="6Lcg7CMUAAAAANphynKgn9YAgA4tQ2KI_iqRyTwd", url="https://lessons.zennolab.com/captchas/recaptcha/v2_nosubmit.php?level=high"))