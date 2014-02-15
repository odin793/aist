# -*- coding: utf-8 -*-

from django import forms
from captcha.fields import ReCaptchaField

class MyCaptchaField(ReCaptchaField):
    default_error_messages = {
       'captcha_invalid': 'Неверно. Попробуйте еще раз.'
    }

class QuestionForm(forms.Form):
    last_name = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    email = forms.EmailField(error_messages={'invalid': 'Введите корректный e-mail'})
    subject = forms.CharField(max_length=200, required=False)
    question = forms.CharField(widget=forms.Textarea, required=True)
    captcha = MyCaptchaField(attrs={'theme': 'clean'})