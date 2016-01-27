from django.contrib import admin

from .forms import SignUpForm
from .models import SignUp, Picture, Post


class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp", "updated"]
    form = SignUpForm
    # class Meta:
    #   model = SignUp


admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Picture)
admin.site.register(Post)
