from django.contrib import admin
from .models import Persons
from .models import Posts
from .models import Media
from .models import Dialogs
from .models import Message
from .models import Friends

# Register your models here.
admin.site.register(Persons)
admin.site.register(Media)
admin.site.register(Posts)
admin.site.register(Dialogs)
admin.site.register(Message)
admin.site.register(Friends)