from django.contrib import admin
from .models import UserModel, ContentModel
# Register models
admin.site.register(UserModel)
admin.site.register(ContentModel)
