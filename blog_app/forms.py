#(https://e-tec-memo.herokuapp.com/article/19/#:~:text=as%20auth_forms%0A%0Aclass-,LoginForm,-(auth_forms.AuthenticationForm)%3A%0A%20%20%20%20%27%27%27%E3%83%AD%E3%82%B0%E3%82%A4%E3%83%B3)
from django.contrib.auth import forms as auth_forms

class LoginForm(auth_forms.AuthenticationForm):
    '''ログインフォーム'''
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label