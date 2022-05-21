from django.contrib import admin
from app.models import Todo,Profile,Category
# Register your models here.
admin.site.register(Todo)
admin.site.register(Profile)
admin.site.register(Category)