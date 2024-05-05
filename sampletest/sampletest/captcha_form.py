from django.forms import ModelForm, Form
from captcha.fields import CaptchaField


class CheckPasswordForm(Form):
    captcha = CaptchaField(label='Введите текст с картинки', error_messages={'invalid':'Неправильный текст'})