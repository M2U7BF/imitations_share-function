from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import User

# django/contrib/auth/forms.py における UserChangeForm の記述の書き換え
class MyUserChangeForm(UserChangeForm):
    # field_classes = {"username": UsernameField} → 削除
    # classオブジェクト を生成するのが Metaで作成するclass(設計書)(https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python)
    # username に関する設定を変更したいのだろうか?
    class Meta:
        model = User
        fields = '__all__'

class MyUserCreationForm(UserCreationForm):
    # field_classes = {"username": UsernameField} → 削除
    class Meta:
        model = User
        fields = ('email','username')

class MyUserAdmin(UserAdmin):
    # 変更
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            # usernameの表記の削除
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    # 独自のものに変更
    form = MyUserChangeForm
    # 独自のものに変更
    add_form = MyUserCreationForm
    # first_name last_name の削除
    list_display = ('email', 'username', 'is_staff')
    # 原文
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    # first_name last_name の削除
    search_fields = ('email', 'username')
    # username → email の変更
    ordering = ('email',)

# 管理画面への表示
admin.site.register(User, MyUserAdmin)