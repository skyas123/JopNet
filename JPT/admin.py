from django.contrib import admin
from .models import Persons
from .models import Posts
from .models import Media
# Register your models here.
admin.site.register(Persons)
admin.site.register(Media)
admin.site.register(Posts)