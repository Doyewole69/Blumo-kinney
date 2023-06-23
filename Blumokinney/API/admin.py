from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm, UserCreationForm
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    add_form = UserCreationForm
    form = UserChangeForm
    ordering = ('email',)

admin.site.register(User, UserAdmin)