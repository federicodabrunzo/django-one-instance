from django.contrib import admin

from testapp.models import *
from one_instance.admin import SingletonAdmin


admin.site.register(Config, SingletonAdmin)
