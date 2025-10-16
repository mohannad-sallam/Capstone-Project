from django.contrib import admin

from .models import Comment, Parts, Profile, Review

admin.site.register(Profile)
admin.site.register(Parts)
admin.site.register(Review)
admin.site.register(Comment)
